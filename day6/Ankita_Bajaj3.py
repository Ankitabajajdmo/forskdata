'''
url = "http://api.openweathermap.org/data/2.5/weather"
url += "?q=Bhopal&appid=27420379caba175e0af5ee69d02dce41"

from urllib.request import urlopen

resp =urlopen(url)   # GET request to REST API

print(resp.read())




import requests

resp = requests.get(url)   # GET request to REST API

print(resp.text)
'''

import requests
url="http://13.127.155.43/api_v0.1/sending"
data = {"Phone_Number":"916264145369",
        "Name":"ANKITA BAJAJ",
        "College_Name":"S.A.T.I vidisha(BHOPAL)",
        "Branch" : "CSE"
        }

send = requests.post(url,json = data)
print(send.text)

req_url="http://13.127.155.43/api_v0.1/receiving?Phone_Number=916264145369" 
recieve=requests.get(req_url )
print(recieve.text)