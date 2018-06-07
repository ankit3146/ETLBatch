import tweepy
import json
import csv

#Twitter Credentials  
consumer_key = "cyztWtw6VHhI9H4xU2LkiE2fp"
consumer_secret = "aYEWeX6w7n9QEgZYlbGPIMCJI3a8CSFIbFjRo6KTBtcMczO4M1"
access_key="1000024551135301632-RVAqwH9nZquPFrpjSyXkO7cTdUB5E8"
access_secret="z4871Z2rxy6oz22R6Kv1H9EDKbAC6kwj7Hy8frch9kayu"

#Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)
screen_name = "5408Csci"

#fetch twitter profile of user
def get_profile(screen_name):
    api = tweepy.API(auth)
    try:
        trends = api.get_user(screen_name)
    except tweepy.error.TweepError as e:
        trends = json.loads(e.response.text)
    return trends


#fetch tweets based on a hashtag
def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = [status for status in tweepy.Cursor(api.search, q=query).items(100)]
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets

trends = get_profile(screen_name)
queries = ["#Canada150"]

#store tweets in csv format
with open ('rawtweets.csv', 'w',encoding="utf8",newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id','user','created_at','text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            print((tweet.id_str))
            writer.writerow([(tweet.id_str),(tweet.user.screen_name),tweet.created_at,(tweet.text)])
            
            
