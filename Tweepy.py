#Scraping Using Tweepy

import tweepy
from tweepy import OAuthHandler

import simplejson as json

consumer_key = "d02tqSUSADhsK2kV2Rrcj3amq"
consumer_secret = "s6UnOqWeEssvS3fk9Pnpcx4MBXDVW198LYsY0unjw9IgIYKVIR"
access_token = "3267212815-TUhrt9RIqARFTyt11SWXxad05EAtYlAfm0nOQh9"
access_secret = "m8MaRmUYF9hos7E56naaeDePWqDCYp5v43ryWZsC7JdKx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
     #Process a single status
     print(status.text)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for status in tweepy.Cursor(api.home_timeline).items():
    process_or_store(friend._json)
