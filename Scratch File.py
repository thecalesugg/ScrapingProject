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


csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

searchTerm = "#SBLIII"
ticker = 0
for tweet in tweepy.Cursor(api.search,
                           q = searchTerm,
                           since = "2018-01-14",
                           until = "2019-05-15",
                           lang = "en").items():

    ticker += 1
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([ticker, searchTerm, tweet.created_at, tweet.in_reply_to_status_id, tweet.retweet_count, tweet.favorite_count, tweet.text.encode('utf-8')])
    print(ticker, searchTerm, tweet.created_at, tweet.in_reply_to_status_id, tweet.retweet_count, tweet.favorite_count, tweet.text)
csvFile.close()