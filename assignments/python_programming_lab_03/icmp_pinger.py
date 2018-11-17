from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8

def checksum(string: str) -> int:
    """Generate the ICMP checksum of the specified string. 

    The checksum is the 16-bit one's complement of the one's complement sum of the ICMP message, starting with the ICMP Type field.
    
    Args:
        string (str): String to checksum
    """
    csum = 0
    count_to = (len(string) // 2) * 2
    count = 0

    while count < count_to:
        this_val = ord(string[count + 1]) * 256 + ord(string[count])
        csum = csum + this_val
        csum = csum & 0xffffffff
        count = count + 2

    if count_to < len(string):
        csum = csum + ord(string[len(string) - 1])
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

def receive_one_ping(my_socket, pid, timeout, destination_addr):
    pass