import requests
url="http://ifconfig.co/ip"
resp=requests.get(url)
print(resp.text)