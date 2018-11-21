Joel Benjamin Castillo (jc5383)  
CS6843 - Computer Networking  
Prof. Rafail Portnoy  
<p align=center><strong>Lab 3: Traceroute Lab</strong></p>

## Python Code (`main.py`)
```python
import socket
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2

def checksum(string: str):
    """Generate a checksum for the ICMP header.
    
    Args:
        string (str): String for checksum
    
    Returns:
        int: Checksum for header
    """

    csum = 0
    count_to = (len(string) // 2) * 2
    count = 0
    while count < count_to:
        cur_val = string[count+1] * 256 + string[count]
        csum = csum + cur_val
        csum = csum & 0xffffffff
        count = count + 2
    if count_to < len(string):
        csum = csum + string[len(string) - 1]
        csum = csum & 0xffffffff
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def build_packet():
    """Generate an ICMP packet for use in the traceroute function
    
    Returns:
        bytes: ICMP Packet (Header + Data)
            Header = Header is icmp_type (8), code (8), checksum (16), id (16), seq (16)

    """    
    packet_checksum = 0

    # Get Current Process PID
    process_pid = os.getpid() & 0xFFFF 

    # Make a dummy header with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, packet_checksum, process_pid, 1)
    
    # Setup data for the packet
    data = struct.pack("d", time.time())

    # Calculate the checksum on the data and the dummy header.
    packet_checksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        
        #Convert 16-bit integers from host to network byte order.
        packet_checksum = socket.htons(packet_checksum) & 0xffff
    else:
        packet_checksum = socket.htons(packet_checksum)

    # Build actual header
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, packet_checksum, process_pid, 1)

    # Build actual packet
    packet = header + data
    return packet

def get_route(hostname):
    """Get the route between the current host and the provided hostname. Outputs route to STDOUT
    
    Args:
        hostname (str): Hostname to trace route to.
    """
    print(hostname)
    time_left = TIMEOUT
    for ttl in range(1,MAX_HOPS):
        for tries in range(TRIES):
            dest_addr = socket.gethostbyname(hostname)
            # Make a raw socket called current_socket
            icmp = socket.getprotobyname("icmp")
            current_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            current_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, struct.pack('I', ttl))
            current_socket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                current_socket.sendto(d, (hostname, 0))
                t = time.time()
                start_select = time.time()
                ready = select.select([current_socket], [], [], time_left)
                select_time_elapsed = (time.time() - start_select)
                if ready[0] == []: # Timeout
                    print(" * * * Request timed out.")
                received_packet, addr = current_socket.recvfrom(1024)
                time_received = time.time()
                time_left = time_left - select_time_elapsed
                if time_left <= 0:
                    print(" * * * Request timed out.")
            except socket.timeout:
                continue
            else:
                # Fetch the ICMP Type from the IP Packet
                icmp_header_content = received_packet[20:28]
                icmp_type, _code, _checksum, _packet_id, _sequence = struct.unpack("bbHHh", icmp_header_content)
                if icmp_type == 11:
                    bytes = struct.calcsize("d")
                    time_sent = struct.unpack("d", received_packet[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" % (ttl, (time_received -t)*1000, addr[0]))
                elif icmp_type == 3:
                    bytes = struct.calcsize("d")
                    time_sent = struct.unpack("d", received_packet[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" % (ttl, (time_received-t)*1000, addr[0]))
                elif icmp_type == 0:
                    bytes = struct.calcsize("d")
                    time_sent = struct.unpack("d", received_packet[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" % (ttl, (time_received - time_sent)*1000, addr[0]))
                    return
                else:
                    print("error")
                break
            finally:
                current_socket.close()


if __name__ == '__main__':
    get_route("www.google.com")
```

## Traceroute Output
<img src="traceroute_screenshot.png" />
