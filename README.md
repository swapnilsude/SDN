# SDN

## Packet Processing
Used wireshark to capture traffic and exported the collected trace to a CSV file.
Used python program to process and get following data:    
+ Total number of TCP connections    
+ Total number of packets in the trace    
+ Total amount of traffic (packet sizes) in the trace    
+ For each TCP connection:   
  - IP address pair   
  - TCP port numbers     
  - Total number of packets in each direction       
  - Total amount of traffic in each direction        
  - Response time (measured from SYN packet to the last packet in the opposite direction)     
