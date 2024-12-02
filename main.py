import os
from dotenv import load_dotenv
import tweepy.client

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_key = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

print(f"api key : {api_key}, api secret : {api_secret}, access_key : {access_key}, access_secret : {access_secret}, bearer_token : {bearer_token}") 

import tweepy 

# auth = tweepy.OAuth1UserHandler(
#     api_key,
#     api_secret,
#     access_key,
#     access_secret
# )

# api = tweepy.API(auth)

# tweets = api.home_timeline(count=4)
# for tweet in tweets:
#     print(tweet.text, '\n')

# auth = tweepy.OAuthHandler(api_key, api_secret)
# auth.set_access_token(access_key, access_secret)

# api = tweepy.API(auth)
# user = api.get_user(screen_name="Twitter")
# client = tweepy.client(bearer_token=)

# followers = api.get_followers()

# print(user.screen_name)

# print(followers)

# for follower in followers:
#     print(f"{follower.screen_name}")
