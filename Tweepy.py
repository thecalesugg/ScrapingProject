#Scraping Using Tweepy

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import simplejson as json
import csv


consumer_key = "d02tqSUSADhsK2kV2Rrcj3amq"
consumer_secret = "s6UnOqWeEssvS3fk9Pnpcx4MBXDVW198LYsY0unjw9IgIYKVIR"
access_token = "3267212815-TUhrt9RIqARFTyt11SWXxad05EAtYlAfm0nOQh9"
access_secret = "m8MaRmUYF9hos7E56naaeDePWqDCYp5v43ryWZsC7JdKx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#CSV File Handling
file = open('SB18.csv','w')
writer = csv.writer(file, delimiter=',', quoting = csv.QUOTE_MINIMAL)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

#Cursor interface iterates through different types of objects
for status in tweepy.Cursor(api.home_timeline).items(10):
      #Process a single status
      print(status.text)

#Gets JSON dump
for status in tweepy.Cursor(api.home_timeline).items(10):
     # Process a single status
     process_or_store(status._json)

#List of Followers
for friend in tweepy.Cursor(api.friends).items(10):
     process_or_store(friend._json)

#List of all tweets
for tweet in tweepy.Cursor(api.user_timeline).items(10):
    process_or_store(tweet._json)

# #CSV Sections
# for tweet in tweepy.Cursor(api.search, q='#SBLIII').items(10):
#     writer.writerow([tweet.created_at])
#     print(tweet.created_at)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#SBLIII'])