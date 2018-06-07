# -*- coding: utf-8 -*-
import pandas as pd
import re
import csv
from textblob import TextBlob

path = ""
df = pd.read_csv(r'D:\Documents\Study\Dalhousie\Summer2018\Data\A2\rawtweets.csv')
y = df['text']

#add polarity score of every word present in tweet
def calculate_sentiments(answer):
        total = 0
        ans = answer.split()
        for an in ans:
            an = TextBlob(an)
            total += an.sentiment.polarity
            print(an.sentiment.polarity, an)
        return total
        
#read data from the csv file    
with open ('cleantweets.csv', 'w',encoding="utf8",newline='') as cleantweets:
    writer = csv.writer(cleantweets)
    writer.writerow(['sentiment','text','score'])
    for t in y:
        #Cleaning of tweets
        #https://stackoverflow.com/questions/14081050/remove-all-forms-of-urls-from-a-given-string-in-python
        t = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
					|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''''', ' ', t)
        print("\n")
        t = re.sub(r'@[A-Za-z0-9]+','',t)
        t = re.sub(r'RT','',t)
        #https://stackoverflow.com/questions/21564625/removing-everything-except-letters-and-spaces-from-string-in-python3-3
        whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        answer = ''.join(filter(whitelist.__contains__, t))
        
        total = calculate_sentiments(answer)
        #calculate the sentiments of query based on total
        if(total>0):
            writer.writerow([('Positive'),(answer),total])
        elif(total==0):
            writer.writerow([('Neutral'),(answer),total])
        else:
            writer.writerow([('Negative'),(answer),total])




