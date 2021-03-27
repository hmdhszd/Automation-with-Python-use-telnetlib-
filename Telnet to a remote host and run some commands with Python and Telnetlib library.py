
import telnetlib
import time


HOST = "128.223.51.103"
username = "rviews"



tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")





tn.write(b"show ip bgp 194.156.140.0 best\n")
time.sleep(2)

  
  
  
    
tn.write(b"exit\n")




MyOutput = tn.read_all().decode('ascii')
print(MyOutput)
    
    
   
