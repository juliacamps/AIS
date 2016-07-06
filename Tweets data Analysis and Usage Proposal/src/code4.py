import tweepy
import csv
import time
import json
from tweepy.parsers import JSONParser
import os

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

consumer_key = 's2dozoBIo8ZXeB85GhtDyEdtA'
consumer_secret = '...'
access_token = '1407291667-FltDU3HGnqPC0esuOtquRCC8bnRyvFJ5Pz928QD'
access_secret = '...'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Open/Create a file to append data
collected_users_path = os.getcwd()+r"\users_dataset.txt"
dataset_path = os.getcwd()+r"\castells_twitter_dataset.json"

with open(collected_users_path, 'rb') as users_file:
   users = ((users_file.read()).decode("utf-8")).split("\n")

count = 0
iter = 359
users = users[iter:]
print(len(users))
new_data = []
with open(dataset_path, 'ab') as dataFile:
    for item in users:
        print(iter)
        raw_tweets = tweepy.Cursor(api.search,
                                   q="from:"+item,
                                   show_user=True,
                                   ).items()
        tweets = [(str(tweet) + "\n") for tweet in raw_tweets]
        tweets = list(set(tweets))
        data = (''.join(tweets)).encode('utf8')
        dataFile.write(data)
        iter += 1
