import tweepy
from tweepy import OAuthHandler


import csv

consumer_key = "d02tqSUSADhsK2kV2Rrcj3amq"
consumer_secret = "s6UnOqWeEssvS3fk9Pnpcx4MBXDVW198LYsY0unjw9IgIYKVIR"
access_token = "3267212815-TUhrt9RIqARFTyt11SWXxad05EAtYlAfm0nOQh9"
access_secret = "m8MaRmUYF9hos7E56naaeDePWqDCYp5v43ryWZsC7JdKx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

searchTerm = "#SBLII -filter:retweets"

'''
tweet = api.get_status(1125742854524084224)
print(tweet.entities.get('hashtags'), tweet.favorite_count, tweet.retweet_count)
'''


for tweet in tweepy.Cursor(api.search,
                           q = searchTerm,
                           since = "2018-01-14",
                           until = "2019-05-15",
                           lang = "en").items(25):
    print(tweet.id, len(tweet.entities.get('hashtags')), tweet.entities.get('hashtags'), tweet.favorite_count, tweet.retweet_count)