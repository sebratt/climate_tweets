# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join
from pymongo import MongoClient


client = MongoClient("mongodb://bitslab:0rang3!@127.0.0.1:27017")
db = client.arxiv_5bfcc8f5060363662992ca4d 

# Define start and end dates: yyyy, m, d, h
start_date = datetime(2018, 11, 2, 0) # Will it break if we define the dates before the collection start?
end_date = datetime(2018, 12, 6, 0) # Will it break if we define the dates after the current day?

    
outfile = './arxiv_sample_2.csv'
csvfile = open(outfile, 'w')
writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(['tweet_id', 'date','screen_name','text'])    
         
tweets = db.tweets.find({"text": {"$regex": "arxiv", "$options": "i"}})

print(tweets.count())
for tweet in tweets:
    tweet_id = ""
    tweet_date = ""
    screen_name = ""
    tweet_text = ""
        
    tweet_id ="ID_"+ str(tweet['id'])
    tweet_date = tweet['created_at']
    screen_name = tweet['user']['screen_name']
    tweet_text = tweet['text'].replace(',', ' ')
               
    writer.writerow([tweet_id, tweet_date,
                     screen_name, tweet_text])

            
        
