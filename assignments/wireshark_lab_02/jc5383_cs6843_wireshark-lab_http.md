Joel Benjamin Castillo (jc5383)  
CS6843 - Computer Networking  
Prof. Rafail Portnoy  
<p align=center><strong>Wireshark Lab - HTTP</strong></p>

## Section 1: The Basic HTTP GET/response Interaction
**NOTE**: This section of the lab was run on a different virtual machine. I accidentally destroyed my VirtualBox machine while running some updates (using Kali Linux). When I rebuilt the machine I switched over to using a `Bridged Network Adapater` as opposed to the default `Host-Only Adapter` so that I could copy the `pcapng` files from my VM to my Windows host for screenshots and further analysis using SSH. For later sections of the lab my IP address is `192.168.1.49` as opposed to `10.0.2.15`.

1. Is your browser running HTTP version 1.0 or 1.1? What version of HTTP is the server running?
Browser: `HTTP v1.1`
<img src="./wireshark_lab-http_s1q1p1.PNG" />
Server: `HTTP v1.1`
<img src="./wireshark_lab-http_s1q1p2.PNG" />
2. What languages (if any) does your browser indicate that it can accept to the server?
Languages: `en-US, en` (In that order)
<img src="./wireshark_lab-http_s1q2.PNG" />
3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?
My Computer: `10.0.2.15`
`gaia.cs.umass.edu`: `128.119.245.12`
<img src="./wireshark_lab-http_s1q3.PNG" />
4. What is the status code returned from the server to your browser?
`200 OK`
<img src="./wireshark_lab-http_s1q4.PNG" />
5. When was the HTML file that you are retrieving last modified at the server?
`Thu, 27 Sep 2018 05:59:01 GMT`
<img src="./wireshark_lab-http_s1q5.PNG" />
6. How many bytes of content are being returned to your browser?
`128 bytes`
<img src="./wireshark_lab-http_s1q6.PNG" />
7. By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window? If so, name one.
There are no additional headers shown in the packet content window.
<img src="./wireshark_lab-http_s1q7.PNG" />

## Section 2: The HTTP Conditional GET/response Interaction
8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an "IF-MODIFIED-SINCE" line in the HTTP GET?
No
<img src="./wireshark_lab-http_s2q8.PNG" />
9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?
Yes - The content is available in the packet contents window. The total size returned by the server is 371 bytes, in 3 frames (highlighted below.)
<img src="./wireshark_lab-http_s2q9.PNG" />
10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an "IF-MODIFIED-SINCE:" line in the HTTP GET? If so, what information follows the "IF-MODIFIED-SINCE:" header?
Yes
`IF-MODIFIED-SINCE: Fri, 28 Sep 2018 05:59:02 GMT`
<img src="./wireshark_lab-http_s2q10.PNG" />
11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.
The status code is `304 Not Modified`
No - The contents of the file were not returned (they are not shown in the packet contents window). Since the file was not modified since the last HTTP request, the contents of the file are just loaded from the browser cache.
<img src="./wireshark_lab-http_s2q11.PNG" />

## Section 3: Retrieving Long Documents
12. How many HTTP GET request messages did your browser send? Which packet number in the trace contains the GET message for the Bill or Rights?
There were two `HTTP GET` requests sent by my browser. No. 49 and No. 59
<img src="./wireshark_lab-http_s3q12p1.PNG" />
The request for the Bill of Rights (`HTTP-wireshark-file3.html`) was No. 49
<img src="./wireshark_lab-http_s3q12p2.PNG" />
13. Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?
No. 57 contains the Response
<img src="./wireshark_lab-http_s3q13.PNG" />
14. What is the status code and phrase in the response?
The phrase is `200 OK`
<img src="./wireshark_lab-http_s3q14.PNG" />
15. How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?
4 TCP Segments
<img src="./wireshark_lab-http_s3q15.PNG" />

##  Section 4: HTML Documents with Embedded Objects
16. How many HTTP GET request messages did your browser send? To which Internet addresses were these GET requests sent?
3 `HTTP GET` requests were sent
    - No. 21 was to `128.119.245.12` - `/wireshark-labs/HTTP-wireshark-file4.html`
    - No. 28 was to `128.119.245.12` - `pearson.png`
    - No. 36 was to `128.119.245.12` - `/~kurose/cover_5th_ed.jpg`
<img src="./wireshark_lab-http_s4q16.PNG" />
17. Can you tell whether your browser downloaded the two images serially, or whether they were downloaded from the two web sites in parallel? Explain.
The images were downloaded serially because there were multiple TCP requests sent out for the images.
<img src="./wireshark_lab-http_s4q17p2.PNG" />
<img src="./wireshark_lab-http_s4q17p2.PNG" />

## Section 5: HTTP Authentication
18. What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?
`401 Unauthorized`
<img src="./wireshark_lab-http_s5q18.PNG" />
19. When your browser’s sends the HTTP GET message for the second time, what new field is included in the HTTP GET message?
`AUthorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=`
<img src="./wireshark_lab-http_s5q19.PNG" />