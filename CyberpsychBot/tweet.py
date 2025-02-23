import os
import time
import tweepy
from generate_tweet import generate_tweet_text

os.environ["ACCESS_KEY"] = os.getenv("ACCESS_KEY")
os.environ["ACCESS_SECRET"] = os.getenv("ACCESS_SECRET")
os.environ["CONSUMER_KEY"] = os.getenv("CONSUMER_KEY")
os.environ["CONSUMER_SECRET"] = os.getenv("CONSUMER_SECRET")
os.environ["BEARER_TOKEN"] = os.getenv("BEARER_TOKEN")

auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(
    os.environ["ACCESS_KEY"],
    os.environ["ACCESS_SECRET"],
)

newapi = tweepy.Client(
    bearer_token= os.environ["BEARER_TOKEN"],
    access_token= os.environ["ACCESS_KEY"],
    access_token_secret= os.environ["ACCESS_SECRET"],
    consumer_key= os.environ["CONSUMER_KEY"],
    consumer_secret= os.environ["CONSUMER_SECRET"],
)

api = tweepy.API(auth)

def tweet():
    try:
        sampletweet = generate_tweet_text()
        
        post_result = newapi.create_tweet(text=sampletweet)
    
    except Exception as e:
        print(f"Tweet couldn't be posted because: {e}")