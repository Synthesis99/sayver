
from dotenv import load_dotenv
load_dotenv()

import tweepy
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


from shadow_drive import ShadowDriveClient
from solders.keypair import Keypair
from urllib.parse import quote
import argparse

import time
from datetime import datetime, timedelta, timezone

import subprocess



def authenticate_twitter_api():
    bearer_token = os.environ.get('BEARER_TOKEN')
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    if not bearer_token or not consumer_key:
        raise ValueError("Missing environment variables")

    # V1 Twitter API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api_v1 = tweepy.API(auth, wait_on_rate_limit=True)

    # V2 Twitter API Authentication
    client_v2 = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True,
    )

    return api_v1, client_v2

api, client = authenticate_twitter_api()

iteration = 0
initial_run = datetime.now(timezone.utc) - timedelta(seconds=60)
print(f"INITIAL RUN STARTED AT {initial_run}")


while True:
    
    iteration += 1
    print (iteration)

    start = initial_run + timedelta(seconds=60 * iteration)
    end = start + timedelta(seconds=60)
    
    start_str = start.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    end_str = end.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    print(f"FINDING MENTIONS FROM {start} TO {end}")


    mentions = client.get_users_mentions('1663528031124701184', 
        max_results=5, 
        expansions=['author_id', 'referenced_tweets.id'], 
        tweet_fields=['created_at'])
        # start_time=start_str,
        # end_time=end_str)


    # Check if there are no mentions
    if mentions is None or not mentions.data:
        print("No new mentions.")
        time.sleep(90)
        continue  # Skip the rest of the loop and start the next iteration

    for mention in mentions.data:  # Assuming mentions have a 'data' attribute containing the list of mention objects
            user_id = mention.id
            tweet_id = mention.id
            author_id = mention.author_id
            author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
    if author:
        screen_name = author.username

    requested_tweet = mentions.includes['tweets'][0]['text']
    # print(requested_tweet)

    # if "https://" in requested_tweet[-25:]:
    #     # print("tweet not yet supported in alpha testing")
    #     reply_reject = "Sorry, this type of tweet is not yet supported in alpha testing."
    #     client.create_tweet(text=reply_reject, in_reply_to_tweet_id=tweet_id)
    #     print(reply_reject)
    #     continue
    #     # time.sleep(60)
    #     # continue  # Skip the rest of the loop and start the next iteration


    for mention in mentions.data:
        referenced_tweets = mention.data['referenced_tweets']
        for referenced_tweet in referenced_tweets:
            referenced_tweet_id = referenced_tweet['id']

            # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id', ''], tweet_fields=['created_at', ''])
            saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id'], tweet_fields=['created_at'])

            # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id', ''])
            print(type(saved_tweet))
            print(saved_tweet)

            created_at = saved_tweet[0]['created_at']
            print(created_at)



            for tweet in saved_tweet:
                if isinstance(tweet, dict) and 'users' in tweet:  # check if the entry is a dictionary and has a 'users' key
                    user = tweet['users'][0]  # assuming there's only one user per entry
                    creator_id = user['id']
                    creator_username = user['username']
                    # print("User ID:", user_id)
                    # print("Username:", username)

                    tweet_link = (f"https://twitter.com/{creator_username}/status/{referenced_tweet_id}")
                    print(f"Found a new request! Saving {tweet_link}")
                    time.sleep(60)




