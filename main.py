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

auth = tweepy.OAuth1UserHandler(
    api_key,
    api_secret,
    access_key,
    access_secret
)


# tweets = api.home_timeline(count=4)
# for tweet in tweets:
#     print(tweet.text, '\n')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
screen_name="prompt_Tunes"

followers = api.get_followers(screen_name=screen_name, count=100)
for follower in followers:
    print(follower.screen_name)
# user = api.get_user(screen_name=screen_name)
# user_id = user.id_str

# print(user_id)

# api = tweepy.API(auth)
# user = api.get_user(screen_name="Twitter")
print('rate limit exceeds here')
# client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret, access_token=access_key, access_token_secret=access_secret, wait_on_rate_limit=True)

# print('here')
# user_id = client.get_user(username='prompt_Tunes').data.id
# # print(user_id)
# print('or maybe here')

# followers = client.get_users_followers(user_id,)

# followers = client.get_users_followers('prompt_Tunes')