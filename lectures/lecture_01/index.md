# Lecture One

#### Date: 09/08/2018
#### Time: 8:30 AM - 10:30 AM

## Course Organization
### Homework
- Suggested Homework Problems for Every Chapter
    - Don't have to be submitted
    - Research the internet
    - ~ 50% of the midterm and final based on these types of problems

### Quizzes
- Unannounced - Normally at the end of the chapter
- 3 Days to complete after end of the chapter

### Wireshark Labs & Programming Assignments
- After running the lab, submit a 1 file to Newclasses

### Late Work
- Two late submissions allowed (50% penalty)
- No makeup for dropped labs, quizzes, or programming assignments

## Goal
- Get a "feel" and terminology
- More depth and detail will come up later in the course
- Approach 
    - Use the Internet as example
  
## Overview
- What’s the Internet?
- What’s a protocol?
- Network edge; hosts, access net, physical media
- Network core: packet/circuit switching, Internet structure
- Performance: loss, delay, throughput
- Security
- Protocol layers, service models
- History

## What is the Intenret: Nuts and Bolts View
- Billions of connected computing devices:
    - Hosts = End Systems
        - Client devices (servers, laptops, mobile phones, etc.)
    - Running *network apps*
- Communication Links
    - Fiber, copper, radio, satellite, etc.
    - Transmission rate: *bandwidth*
        - Size of the pipe
- Packet Switches
    - Forward packets (chunks of data)
    - *Routers* and *Switches*
- ***Internet: Network of Networks***
    - Interconnected ISPs
- ***Protocols*** control sending, receiving of messages
    - e.g., TCP, IP, HTTP, Skype,  802.11
- ***Internet  standards***
    - RFC: Request for comments
    - IETF: Internet Engineering Task Force

## What is the Internet: A Service View
- *Infrastructure that provides services to applications*
    - Web, VoIP, Email, Games, E-Commerce, Social Networks, etc.
- *Provides a programming interface to apps*
    - Hooks that allow sending and receiving app programs to "connect" to the internet
    - provides service options, analogous to postal service

## What is a Protocol?
- Human Protocols
    - "What is the time?"
    - "I have a question?"
    - Introductions...
    - ... specific messages sent
    - ... specific actions taken when messages received, or other events
- Network Protocols
    - Machines rather than humans
    - All communication activity in Internet governed by protocols
- **Protocols define format and order of messages sent and received among network entities as well as the actions taken on message transmisison and receipt**
  
## A Closer Look at Network Structure
- Network Edge: 
    - Hosts: Clients and Servers
    - Servers are often in data centers
- Access Networks / Physical Media
    - Wired
    - Wireless
    - Communication Links
- Network Core
    - Interconnected routers
    - Network of networks
- How to develop network structure
    - Based on business needs

## Access Network: Digital Ssubscriber Line (DSL)
- Use *existing* telephone line to central office DSLAM
    - Data over DSL phone line goes to internet
    - Voice over DSL phone line goes to telephone network
- < 2.5 Mbps upstream transmission rate (typically < 1 Mbps)
- < 24 Mbps downstream transmission rate (typically < 10 Mbps)
- Voice and data are transmitted at different frequencies over *dedicated* line to central office

## Access Netowrk: Cable Network
- *Frequency Division Multiplexing*: Different channels transmitted in different frequency bands
- HFC: Hybrid Fiber Coax
    - Asymmetric: Up to **30 Mbps** downstream transmission rate, 2 Mbps upstream transmission rate
- Network of cable and fiber attaches home to ISP router
    - Homes *share access network* to cable headend
    - Unlike DSL, which has dedicated access to central office
  
## Access Network: Home Network

## Enterprise Access Networks (Ehternet)
- Typically used in companies, universities, etc.
- 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps transmission rates
- Today, end systems typically connect into an Ethernet switch

## Wireless Access Networks
- Shared wireless access network connects end system to router
    - Via base station (aka Access Point)

## Host: Sends *packets* of data
- Host sending function
    - Takes application message
    - Breaks into smaller 