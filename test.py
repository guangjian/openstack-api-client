#!/usr/bin/python                                                                                                                   
import httplib
import json

# arguments                                                                                                                         
## make sure that url is set to the actual hostname/IP address,                                                                     
## port number                                                                                                                      
#url = "135.251.0.109:8080"                                                                                                         
#url = "135.251.218.126:8774"                                                                                                       
#url = "135.251.208.74:5000"                                                                                                        
url = "135.251.208.74:35357"
username = "test"

## make sure that osuser is set to your actual username, "admin"                                                                    
## works for test installs on virtual machines, but it's a hack                                                                     
osuser = "admin"
## use something else than "shhh" for you password                                                                                  
ospassword = "h0r1z0n"
#params = '{"passwordCredentials":{"username":osuser, "password":ospassword}}'                                                      
params = '{"auth":{"passwordCredentials":{"username":"admin", "password":"h0r1z0n"}}}'
headers = {"Content-Type": "application/json"}
# HTTP connection                                                                                                                   
conn = httplib.HTTPConnection(url)

conn.request("POST", "/v2.0/tokens", params, headers)
# HTTP response                                                                                                                     
response = conn.getresponse()
data = response.read()
print "Response is: %s \n" % data
dd = json.loads(data)
print "json is: %s \n" % dd
conn.close()
#apitoken = dd['auth']['token']['id']                                                                                               
# apitoken = dd['access']['token']['id']
# print "Your token is: %s" % apitoken

user_id = dd['access']['user']['username']
print "user name is: %s" % user_id
print ""
