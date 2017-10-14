import tweepy
from textblob import TextBlob

consumer_key='YOUR CONSUMER KEY'
consumer_secret='YOUR CONSUMER SECRET KEY'

access_token_key='YOUR ACCESS TOKEN KEY'
access_token_secret='YOUR SECRET ACCESS TOKEN KEY'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)

pubic_tweets=api.search('IPL')

for tweet in pubic_tweets:
    print (tweet.text)
    analysis= TextBlob(tweet.text)
    print (analysis.sentiment)
    

