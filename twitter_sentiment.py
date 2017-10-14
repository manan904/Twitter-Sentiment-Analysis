import tweepy
from textblob import TextBlob

consumer_key='ifyY8G0ZlemHkR5v8OzkyrAie'
consumer_secret='hqJEPy5XVNOC4SoDZUvo73SUC2nQv6VFxWR65f14bMxOvOkfKk'

access_token_key='1374479330-rnwp6R5xbPo7q5N2ycsCotVCL6EkZaYbdI0cqJJ'
access_token_secret='s0mmjfp1oajY9dhlQ50cV6ssEnrrKYKqacFymWna5pmlJ'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)

pubic_tweets=api.search('IPL')

for tweet in pubic_tweets:
    print (tweet.text)
    analysis= TextBlob(tweet.text)
    print (analysis.sentiment)
    

