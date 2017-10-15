import tweepy
from textblob import TextBlob
import csv
import sys
import pandas

consumer_key='4o6HarvVFGXNEExm8HB0GWDp1'
consumer_secret='OKQu1iMQOSbOmj2CsAfI272MkPJ6Djyo7SpEyK7WRW1vCMa9XI'

access_token_key='1374479330-KP9bzNZwcan12jlHFK12DBWlTFPCxUAfwp826li'
access_token_secret='MIxfMo3fBU6e7YbqeaPq01Gevivzzc3LWOgUlg4qAhmWv'

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