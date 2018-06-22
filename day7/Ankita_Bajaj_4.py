import tweepy

CONSUMER_KEY ="nX00YvCNP7XrYZGLwOEW1VE39"
CONSUMER_SECRET = "ZBOkqI7nFHudBpL6XgxI7HCKJorjdhAqxqa5j2EUuSmTFggDN1"   
ACCESS_KEY = "825396273062694912-F4BqD61aHk3bP8JtkSj4hB4ONQCSL2W"    
ACCESS_SECRET = "ZmsNvYqwFwA4CqfM1Yz68jilFPWRZVvAWwoj5PX4PIeXD"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


api.update_status('Ankita testing api-Updating using OAuth authentication via Tweepy!')
#************************************************


import twitter
api = twitter.api(consumer_key = CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_KEY, access_token_secret=ACCESS_SECRET)
print(api.GetFollowers())
#*********************************

import oauth2
from twitter import Twitter
  # ...
twitter = Twitter(auth= oauth2(ACCESS_KEY,ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
  # Get the public timeline
  #twitter.statuses.public_timeline()
print(twitter.GetFollowers())

#***************************************

import twitter
api = twitter.Api(consumer_key="xxxxxxxxxxxx", consumer_secret="xxxxxxxxxxxxxx",
                  access_token_key="314746354-xxxxx", access_token_secret="xxxxxx")
 
user = "@TutsPlusCode"
statuses = api.GetUserTimeline(
    screen_name=user, count=30, include_rts=False)
for s in statuses:
    print(s.text)