url="https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY"


API_KEY="AIzaSyDvmSmPrjGMryQBDjZ7SeZoNu2dfUOm2p8"
client_id="81420296654-58f4kf9j9s9v6v7sv674dflalbd70ofb.apps.googleusercontent.com"
client_sectret_key="cv9EKNMzePgQcyOyBissUSLa"


import json, urllib
url="https://maps.googleapis.com/maps/api/directions/json?"
API_KEY="AIzaSyDvmSmPrjGMryQBDjZ7SeZoNu2dfUOm2p8"
origin=input("start : ")
destination=input("dest : ")
nav_req = "origin={}&destination={}&key={}".format(origin,destination,API_KEY)

req = url + nav_req
ur = urllib.request.urlopen(req)
result = json.load(ur)
print(result)

#******************************************
d={}
d["origin"]=input("origin : ")
d["destination"]=input("Destination : ")
d["key"]=API_KEY
url=url+str(d)
#******************************************

import googlemaps
start = "sitapura,navodaya girls hostel jaipur"
finish = "forsk technologies,jaipur,rajasthan"
url = 'http://maps.googleapis.com/maps/api/directions/json?%s' %urllib.parse.urlencode((
            ('origin', start),
            ('destination', finish)
 ))
ur = urllib.request.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
    print(j)