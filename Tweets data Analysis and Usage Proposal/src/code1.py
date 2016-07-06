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
# places = api.geo_search(query="Spain", granularity="country")
# place_id = places[0].id
#
# tweets = api.search(q="place:%s" % place_id)
# for tweet in tweets:
#     print(tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place")


# Open/Create a file to append data
jsonPath = os.getcwd()+r"\raw_dataset.json"

constructions = """2de6 OR Pde5 OR 9de6 OR 4de7 OR 3de7 OR 3de7a OR 4de7a
OR 7de7 OR 5de7 OR 7de7a OR 5de7a OR 3de7s OR 9de7 OR 2de7 OR 4de8
OR Pde6 OR 3de8 OR 7de8 OR 2de8f OR Pde7f OR 5de8 OR 4de8a OR 3de8a
OR 7de8a OR 5de8a OR 4de9f OR 3de9f OR 9de8 OR 3de8s OR 2de9fm
OR Pde8fm OR 7de9f OR 5de9f OR 4de9fa OR 3de9fa OR 4de9sf OR 2de8sf
OR 3de10fm OR 4de10fm OR 2de9sm OR Pde9fmp OR 3de9sf OR 2d6 OR Pd5
OR 9d6 OR 4d7 OR 3d7 OR 3d7a OR 4d7a OR 7d7 OR 5d7 OR 7d7a OR 5d7a
OR 3d7s OR 9d7 OR 2d7 OR 4d8 OR Pd6 OR 3d8 OR 7d8 OR 2d8f OR Pd7f OR 5d8
OR 4d8a OR 3d8a OR 7d8a OR 5d8a OR 4d9f OR 3d9f OR 9d8 OR 3d8s OR 2d9fm
OR Pd8fm OR 7d9f OR 5d9f OR 4d9fa OR 3d9fa OR 4d9sf OR 2d8sf OR 3d10fm
OR 4d10fm OR 2d9sm OR Pd9fmp OR 3d9sf"""
vocabulary = """Agulla OR Aixecador OR Acotxador OR Baixos OR Contrafort
OR Crossa OR Dosos OR Dau OR Enxaneta OR Folre OR Laterals OR Manilles
OR pinya OR Puntals OR Tronc OR Vents OR Pom OR Primeres"""
translations = "castells OR castell OR casteller OR tower OR towers OR humantowers"

query = translations + " OR " + vocabulary + " OR " + constructions
queries = query.split(" OR ")
count = 0
iter = 96
queries = queries[iter:]
print(len(queries))
new_data = []
with open(jsonPath, 'ab') as jsonFile:
    for item in queries:
        print(iter)
        raw_tweets = tweepy.Cursor(api.search,
                                   q=item,
                                   geocode="41.4165954590,2.1845753193,300km",  # 255.35km",
                                   show_user=True,
                                   ).items()
        tweets = [(str(tweet) + "\n") for tweet in raw_tweets]
        tweets = list(set(tweets))
        data = (''.join(tweets)).encode('utf8')
        jsonFile.write(data)
        iter += 1

