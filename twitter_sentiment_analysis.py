
# coding: utf-8

# In[5]:

import tweepy
from textblob import TextBlob

consumer_key= 's4borchM2lvJlDvmQDylZfMbf'
consumer_secret= 'B0USjG7OKRTJyKvXHUg9JjgOtpWF35rWr8w1LQIRRitlJ4KyaA'

access_token= '2250241622-hc2lSZAF8l3lqZuiSdbbWiJBrjJLvAsNuORfz8i'
access_token_secret= 'S96qrlnewNtcFsknOPm047yEY319rESzHSJHrklmZrBDF'


auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

#search for tweets with a keyword

public_tweets= api.search('Trump')
for tweet in public_tweets:
	print (tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)
#polarity measures how +ve or -ve some text is and subjectivity means factual vs opinion


# In[ ]:



