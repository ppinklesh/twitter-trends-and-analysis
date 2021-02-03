


#tweets trends and count
import sys
import tweepy
import json
# import auth_data
from auth_data import consumer_key, consumer_secret, access_token, access_token_secret
trendList = []

#Autenticate
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where On Earth ID for India is 23424848.
INDIA_WOE_ID = 23424848

INDIA_WOE_ID = api.trends_place(INDIA_WOE_ID)
# INDIA_WOE_ID = tweepy.API.trends_place(23424848)

trends = json.loads(json.dumps(INDIA_WOE_ID, indent=1))
# print(trends)

for trend in trends[0]["trends"]:
    if trend["name"][0]=='#':
        trendList.append(trend["name"])
        
for trend_count in trendList:
    new_search =  trend_count+'-filter:retweets'
    for tweet in tweepy.Cursor(api.search,q=new_search).items():
        count = len(tweet.text)
        print(trend_count,':',count)
        break