import tweepy
from textblob import TextBlob
import csv
import sys
import pandas

consumer_key='YOUR CONSUMER KEY'
consumer_secret='YOUR CONSUMER SECRET KEY'

access_token_key='YOUR ACCESS TOKEN KEY'
access_token_secret='YOUR SECRET ACCESS TOKEN KEY'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)
topicname='Football'
pubic_tweets=api.search(topicname)
data=[]
for tweet in pubic_tweets:
    text=tweet.text
    #print (TextBlob(tweet.text).tags)
    analysis= TextBlob(tweet.text)
    #print (analysis.sentiment)
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    #print (polarity)
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=text
    data.append(dic)
df=pd.DataFrame(data)
print (df)
df.to_csv('output.csv')
