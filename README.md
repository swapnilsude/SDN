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
   
## Mininet Sample Topology
Python program to create a linear network programmatically with 20 switches in tandem named sw1 to sw10. Connected one host to each switch such that the host connected to switch sw<i> is named h<i> with the delay set between sw<i> and h<i> to i*10ms and the delay for links between switches to 5ms. 
