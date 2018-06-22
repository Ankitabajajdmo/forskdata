import requests

url="http://api.openweathermap.org/data/2.5/weather?appid=27420379caba175e0af5ee69d02dce41&q="
city=input()

url=url+city

json_data=requests.get(url).json()
print(json_data["weather"][0]["main"])