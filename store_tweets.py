# -*- coding: utf-8 -*-
import csv
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

#Read cleaned tweets
with open('cleantweets.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#Store the tweets from csv in json format
with open('tweets.json', 'w') as f:
    json.dump(rows, f)
    
#Elasticsearch
es = Elasticsearch()

#Bulk insert of tweets in elasticsearch
with open('tweets.json') as data_file:    
    data = json.load(data_file)
    for i in data:
        actions = [{"_index": "tweet_data","_type": "sentiment",
                    "_source": {"sentiment":i['sentiment'],
                                "text": i['text'],
                                "score": i['score'],
                                "timestamp": datetime.now()}}]
        helpers.bulk(es, actions)