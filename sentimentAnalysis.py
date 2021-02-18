#perception towards #JoeBiden
from tweepy import API,  OAuthHandler
from textblob import TextBlob
from auth_data import consumer_key, consumer_secret, access_token, access_token_secret

# twiter auth keys
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

#removing spacial charectors and hyperlinks from tweets
def clean_tweets(tweet):
    tweet_words = str(tweet).split(' ')
    clean_words = [word for word in tweet_words if not word.startswith('#')]
    return ' '.join(clean_words)

#analyzing the data for Sentiment Analysis
def analyze(Topic):
    positive_tweets, negative_tweets = [], []
    authentication = OAuthHandler(consumer_key, consumer_secret)
    api = API(authentication)
    public_tweets = api.search(Topic, count=100)
    cleaned_tweets = [clean_tweets(tweet.text) for tweet in public_tweets]
    for tweet in cleaned_tweets:
        tweet_polarity = TextBlob(tweet).sentiment.polarity
        if tweet_polarity<0:
            negative_tweets.append(tweet)
            continue
        positive_tweets.append(tweet)
    return positive_tweets, negative_tweets

hashtag = input('Enter hashTag with # as suffix')
positive, negative = analyze(hashtag)
# print(positive , '\n\n', negative)
length_of_positive = len(positive)
length_of_negative = len(negative)
print(len(positive), ' VS  ', len(negative))
if length_of_positive>length_of_negative:
    print('perception is positive towards',hashtag)
else:
    print('perception is negative towards', hashtag)