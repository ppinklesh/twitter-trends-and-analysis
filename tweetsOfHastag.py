#HashTag latest 100 tweets
import tweepy
from auth_data import consumer_key, consumer_secret, access_token, access_token_secret

####input your credentials here
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

hasHTag = input('enter hashTag with # as suffix ')
#search hastag - retweets are filtered
new_search =  hasHTag +'-filter:retweets'

# loop for searching tweets
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,lang = 'en').items():
    length = len(tweet.text)
    if length == 100:
        break
    else:
        print (tweet.text)