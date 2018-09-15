# Lecture One

#### Date: 09/15/2018
#### Time: 8:30 AM - 10:30 AM

## The Network Core
- Mesh of interconnected routers
- Packet Switching - Hosts break application-layer messages into packets
    - Forward packets from one router to the next, across links on the path from source to destination
    - Each packer transmitted at full link capacity

## Packet Switching: Store-and-Forward
- Takes *L/R* seconds to transmit (push out) *L*-bit packet into a link at *R* bps
- **store and forward**: Entire packet must arrive at the router b efore it can be transmitted on the next link
- End-to-End Delay = *2L/R* 


## Packet Switching: Queuing Delay and Loss
- If arrival rate (in bits) to link exceeds transmission rate of the link for a period of time
    - Packets will queue and wait to be transmitted on the link
    - Packets can be dropped (lost) if the memory buffer fills up

## Two Key Network-Core Functions
- Routing - Determines source and destination route taken by packets
    - Routing Algorithms
- Forwarding - Move packets from router's input to appropriate router output

## Alternative Core: Circuit Switching
- End-to-End Resources allaocated to and reserver for "call" between source & destination
- Dedidcated resources - there is no sharing
    - Circuit-like (guaranteed) performance
- Circuit segment is idle if not used by call (no sharing)
- Commonly used in traditional telephone networks

## Circuit Switching - FDM vs TDM
- FDM - Frequency Division Multiplexing
    - Network links are divided by non-overlapping frequency bands
- TDM - Time Division Multiplexing
    - Access to the link is divided into segments of time where each client can make calls on the dedicated link at specific time interavls.

## Packet Switching vs. Circuit Switching
- Packet switching allows more users to use the network
- Example:
    - 1 Mb/s Link
    - Each user:
        - 100 kb/s when active
        - Active 10% of the time
    - Circuit Switching Capacity - 10 Users
    - Packet Switching Capacity: with 35 users, probability > 10 active at the same time is less than .0004
    - How did we get the value `.004`
    - What happens if `> 35` users?
- Is packet switching a "slam dunk winner"?
    - Great for bursty data 
        - Resource Sharing 
        - Simpler, no call setup
    - **Excessive congestion is possible**: Packet delay and loss
        - Protocols needed for reliable data transfer, congestion control.
            - Ex. Packet Tagging
    - *Q*: How to provide circuit-like behavior?
        - Bandwidth guarantees needed for audio/video apps
        - Still an unsolved problem (Chapter 7)
- *Q:* What are some human analogies of reserved resources (circuit switching) vs. on-demand allocation (packet switching)?\

## Internet Structure: Network of Networks
- End systems connect to Internet via access ISPs (Internet Service Providers)
    - residential, company and university ISPs
- Access ISPs in turn must be interconnected. 
so that any two hosts can send packets to each other
- Resulting network of networks is very complex
    - evolution was driven by economics and national policies
- Let’s take a stepwise approach to describe current Internet structure
- Question: Given *millions* of access ISPs, how do we connect them together?
    - **Option 1**: Connnect each access ISP to every other ISP?
        - Connecting each access ISP to each other directly *doesn't scale*: O(N^2) connections
    - **Option 2**: Connect each access ISP to one global transit ISP (Global ISP)
        - *Customer* and *Provider* ISPs have economic agreement
        - If one global ISP is a viable business, there will be competitors which must be interconnected
        - Internet Exchange Points - Connection point between ISPs (hoteling)
            - Regional networks arise to connect access nets to ISPs