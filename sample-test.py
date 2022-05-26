#server 1 - port 8443
#server 1 - DB - 1526
#Web - 443
import os
import paramiko
import re
username = "root"
password = "pass"
obj-server = connect("server1", "443", username,password)
obj-server.exec_cmd('ps -ef | grep  "DB"  ')
obj-server.exec_cmd('ps -ef | grep  "Web" ')
response = os.cmd("wget server1:443")
if(re.match(response,"Not responding")):
    print("Web server is down ")
else:
    print("Web server is Up and running ")

if(re.match(response,))


obj.exex_cmd()