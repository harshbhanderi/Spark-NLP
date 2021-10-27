 
import requests
import json
 
# hookurl='http://192.168.1.65:2222/'
# hookurl='http://avastar.com'
hookurl='http://100.16.171.239:12345'
 
data={'Name':'NICK','Site':'XoX'}

r=requests.post(hookurl,data=json.dumps(data),headers={'Content-Type':'application/json'})  
print(r)

 