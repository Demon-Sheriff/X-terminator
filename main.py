import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_key = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

print(f"api key : {api_key}, api secret : {api_secret}, access_key : {access_key}, access_secret : {access_secret}") 

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

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

followers = api.get_followers()

# print(followers)

for follower in followers:
    print(f"{follower.screen_name}")
