import requests
API_KEY="AIzaSyDvmSmPrjGMryQBDjZ7SeZoNu2dfUOm2p8"
url="https://maps.googleapis.com/maps/api/directions/json?"

origin = "sitapura,navodaya girls hostel jaipur"
destination = "forsk technologies,jaipur,rajasthan"
nav_req = "origin={}&destination={}".format(origin,destination)
req = url + nav_req
ur=requests.get(req)
x=ur.json()