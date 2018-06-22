Consumer_Key_API_Key="nX00YvCNP7XrYZGLwOEW1VE39"
Consumer_Secret_API_Secret="ZBOkqI7nFHudBpL6XgxI7HCKJorjdhAqxqa5j2EUuSmTFggDN1"

Access_Token="825396273062694912-F4BqD61aHk3bP8JtkSj4hB4ONQCSL2W"
Access_Token_Secret="ZmsNvYqwFwA4CqfM1Yz68jilFPWRZVvAWwoj5PX4PIeXD"

twitter_api="https://api.twitter.com/1.1/search/tweets.json"

import oauth2
import time
import json

params={
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key=Consumer_Key_API_Key, secret=Consumer_Secret_API_Secret)

token = oauth2.Token(key=Access_Token,secret=Access_Token_Secret)

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key

params["q"] = input("enter query on twitter: ")


#Making a Authentication Request
req = oauth2.Request(method="GET", url=twitter_api, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()


from urllib.request import  urlopen
response = urlopen(url)

data =json.load(response)
for i in range(1,5):
    print(i+1,data["statuses"][i]["text"])

#Handling Response

filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()