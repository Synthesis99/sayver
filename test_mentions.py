import tweepy

import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

import time
from datetime import datetime, timedelta, timezone


# Enter API tokens below
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMPEqAEAAAAABIgPfPZJxWHDHDFr5YzXdFKp5JI%3DTGEqa01fpBuFUb7uuVp5JsAYaDJ920bSHouqzMrnTXsNEnnQAx'
consumer_key = 'mDMPRpHgt8lv8u7NUBHOG4gZQ'
consumer_secret = 'p4tqDQkkB8W0cZz5Dg5lwkXN1KoarJWY2n3wbfjvnwU6cCqGlK'
access_token = '1663528031124701184-LGB7JT57SZGo0ZGk9ZBL05Maw3ISgv'
access_token_secret = 'egNV1E5Z8lxsRiJRSo4mZxpN54pbTJ1Xf5nXjv4L4gs0X'


# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True,
)

# iteration = 0
# initial_run = datetime.now(timezone.utc) - timedelta(seconds=120)
# print(f"INITIAL RUN STARTED 2 MINS AGO AT {initial_run}")

    
# iteration += 1
# print (iteration)


# start = initial_run + timedelta(seconds=60 * iteration)
# end = start + timedelta(seconds=60)
    
# start_str = start.strftime('%Y-%m-%dT%H:%M:%S.000Z')
# end_str = end.strftime('%Y-%m-%dT%H:%M:%S.000Z')
# print(f"FINDING MENTIONS FROM {start} TO {end}")


mentions = client.get_users_mentions('1663528031124701184', 
    max_results=5, 
    expansions=['author_id', 'referenced_tweets.id'])
        # start_time=start_str,
        # end_time=end_str)


    # # Check if there are no mentions
    # if mentions is None or not mentions.data:
    #     print("No new mentions.")
    #     time.sleep(60)
    #     continue  # Skip the rest of the loop and start the next iteration


# If there are mentions, iterate through them
for mention in mentions.data:
    referenced_tweets = mention.data['referenced_tweets']
    for referenced_tweet in referenced_tweets:
        referenced_tweet_id = referenced_tweet['id']

    for mention in mentions.data:  # Assuming mentions have a 'data' attribute containing the list of mention objects
            user_id = mention.id
            tweet_id = mention.id
            author_id = mention.author_id
            author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
    if author:
        screen_name = author.username

    requested_tweet = mentions.includes['tweets'][0]['text']

    # print(requested_tweet)
    print(mentions.includes['tweets'])



        # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id'])
        # print(saved_tweet)

#         for tweet in saved_tweet:
#             if isinstance(tweet, dict) and 'users' in tweet:  # check if the entry is a dictionary and has a 'users' key
#                 user = tweet['users'][0]  # assuming there's only one user per entry
#                 creator_id = user['id']
#                 creator_username = user['username']
#                 # print("User ID:", user_id)
#                 # print("Username:", username)




# #         # print(f"Found a new request! Save this: https://twitter.com/sayver_cc/status/{referenced_tweet_id}")
# #         # time.sleep(60)

# #         # Define the screenshot path here using the tweet ID
# #         screenshot_path = f"{referenced_tweet_id}.png"

# # # for tweet in mentions.includes['tweets']:
# # # for tweet in mentions.includes['tweets'][0]['text']:
# # #     print(tweet)

# # # requestor_id = mentions.includes['users'][0]['id']
# # # requestor_handle = mentions.includes['users'][0]['username']

# # # print(requestor_id)
# # # print(requestor_handle)


# # requested_tweet = mentions.includes['tweets'][0]['text']
# # print(requested_tweet)

# # # if "https://" in requested_tweet[-25:]:
# # #     print("tweet not yet supported in alpha testing")

# #     # print(mentions)
    

# #     # Assuming the response object is stored in a variable named "response"
# #     # tweet_text = data['includes']['tweets'][0]['text']
# #     # print(tweet_text)


# #     # /////////////////////

# #     # # Iterate over each mention and reply with the uploaded photo
# #     # for mention in mentions.data:  # Assuming mentions have a 'data' attribute containing the list of mention objects
# #     #     user_id = mention.id
# #     #     tweet_id = mention.id
# #     #     author_id = mention.author_id
# #     #     author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
# #     # if author:
# #     #     screen_name = author.username
# #     #     reply_text = f"@{screen_name} Tweet saved!"



# #         # print(mention.author_id)
# #         # print(reply_text)

# #         # client.create_tweet(text=reply_text, media_ids=[media_id], in_reply_to_tweet_id=tweet_id)





# #         # ////////////////////////////////



# #         # result of print(mentions):


# #         # Response(data=[<Tweet id=1710495392700469249 text='@Zeneca @sayver_cc'>, <Tweet id=1710324150747951202 text='@WhaleChart @sayver_cc'>, <Tweet id=1710321358465544661 text='@WatcherGuru @sayver_cc'>, <Tweet id=1710321084602667339 text='@SolanaSensei @sayver_cc'>, <Tweet id=1710320929891639728 text='@CryptoVonDoom @sayver_cc'>], includes={'users': [<User id=1468881882167185408 name=Hunch username=hunch_nft>], 'tweets': [<Tweet id=1704547354152681526 text='I just want to say how absolutely wonderful it has been to be an advisor for Sugartown for the last year-ish\n\nMost projects that hire me as an advisor largely want to leverage my name and reach\n\nThey ask me "can you please RT our announcement posts? And tweet this, that, and the… https://t.co/vD3O2YvhUN https://t.co/TSC9827wj1'>, <Tweet id=1710317979148157288 text='JUST IN:\n\n\u200bBinance and CEO Changpeng Zhao file motion to get SEC lawsuit dismissed.'>, <Tweet id=1710300228094435660 text='Elon Musk says X (Twitter) will remove the like &amp; retweet button from the timeline. https://t.co/RXPLvSgJ8P'>, <Tweet id=1709954845778587710 text='No matter how much I grow, I will never outsource my tweets, DMs or likes, etc. \n\nAll personal interactions between you and this profile will be with me, Sensei.\n\nMy intern and secretary help me out with all the management or research.'>, <Tweet id=1709963930162884634 text='GM to the survivors. https://t.co/T6n8gPiRia'>]}, errors=[], meta={'result_count': 5, 'newest_id': '1710495392700469249', 'oldest_id': '1710320929891639728', 'next_token': '7140dibdnow9c7btw480ih59zwqzw8bv0cx16lltanjug'})
# #         # 