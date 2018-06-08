# ETLBatch

### Installation Guide:
1. Install Elasticsearch in AWS Instance
2. Install Python in AWS Instance
3. Install textBlob library (Lexicons) in AWS Instance
4. Upload python files in AWS Instance and run them
5. Run the srcipt.sh file for the batch process (i.e. Combines the working of all the three python files) 

### Code Snippets: 
#### fetch_tweets.py:
This code is used to authenticate to the twitter app using consumer_key, access_key, consumer_secret, and access_secret and the get_profile() is used to connect to the twitter account (user profile name). get_tweets is used to fetch the tweets for the defined hashtag using tweepy API and the limit is set to 100 tweets per request.The final part of twitter tweet extraction process is to save tweets in a csv format. Only ‘id’, ‘user’, ‘created_at’ and ‘text’ is saved in the csv file. 

#### clean_tweets.py:
Before running the sentiment analysis algorithm, tweets need to be cleaned from the unnecessary part such as ‘HTML links’, ‘usernames’, ‘RT’, undefined symbols. The code cleans the tweets before running sentiment algorithm.The below snippet is used to calculate the sentiment score of each word in a tweet. After adding the score for each word, the final score for the tweet is calculated.Once the sentiment score of the tweets is obtained, they are classified as Positive, Negative and Neutral. The sentiment score, tweet and sentiment are then stored in a csv file.

#### store_tweets.py
Foremost part of loading the sentiment data in Elasticsearch is to convert it into JSON. This code converts the csv file to json data. Once the json data is ready, the tweet sentiments are stored in elasticsearch db using the elasticsearch library of python. 
This code stores the sentiment data at
**URL**: ec2-instance_name:9200
**Index**: tweet_data
**type**: sentiment

To check if the elasticsearch data is loaded properly or not, open
http://ec2-instance_name:9200/tweet_data/_search

#### script.sh
A shell script is developed which automates the task of fetching the tweets, cleaning them and storing the sentiment data in ElasticSearch DB. The below script runs batch
