import tweepy
from tweepy import OAuthHandler


import csv

#Personal Twitter API Tokens
consumer_key = "d02tqSUSADhsK2kV2Rrcj3amq"
consumer_secret = "s6UnOqWeEssvS3fk9Pnpcx4MBXDVW198LYsY0unjw9IgIYKVIR"
access_token = "3267212815-TUhrt9RIqARFTyt11SWXxad05EAtYlAfm0nOQh9"
access_secret = "m8MaRmUYF9hos7E56naaeDePWqDCYp5v43ryWZsC7JdKx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#Opens CSV File. In between runs, change the name of the file
csvFile = open('SBLII.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

#Change the search term to whatever you need to search for
searchTerm = "#SBLII" # <---- Change This

ticker = 0  #This variable helps you count your Tweets in CSV
for tweet in tweepy.Cursor(api.search,
                           q = searchTerm,
                           since = "2018-01-14",
                           until = "2019-05-10",  #Twitter API only allows free acounts to go seven days back
                           lang = "en").items():  # <--- If you need to limit the amount, put that in the items(amount)

    ticker += 1
    # Write a row to the CSV file.
    csvWriter.writerow([ticker,
                        searchTerm,
                        tweet.created_at,
                        tweet.id,
                        tweet.in_reply_to_status_id,
                        tweet.retweet_count,
                        tweet.favorite_count,
                        tweet.text,
                        len(tweet.entities.get('hashtags')),  #Amount of Hashtags in the tweet
                        tweet.entities.get('hashtags')])
    print(ticker,
          searchTerm,
          tweet.created_at,
          tweet.id,
          tweet.in_reply_to_status_id,
          tweet.retweet_count,
          tweet.favorite_count,
          tweet.text,
          len(tweet.entities.get('hashtags')),
          tweet.entities.get('hashtags'))
csvFile.close()  #Closes the file