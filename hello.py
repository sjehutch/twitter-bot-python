#!/usr/bin/env python
import tweepy
import time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
twt = api.search(q="Amazon Web Services" , count=1 , lang="en" , result_type="recent" , filter="safe")

#list of specific strings we want to check for in Tweets


for s in twt:
	sn = s.user.screen_name
	m = "@%s Awesome Tweet on AWS" % (sn)
	pic = api.media_upload('aws.png')
	s = api.update_status(m, s.id, media_ids=[pic.media_id_string])
	time.sleep(1000000)
print("All done!")
