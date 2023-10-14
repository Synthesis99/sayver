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



# start_time = datetime.datetime.now()
iteration = 0
start_time = datetime.now(timezone.utc) - timedelta(seconds=120)


print(f"INITIAL RUN STARTED 2 MINS AGO AT {start_time}")

iteration += 1
next_time = start_time - timedelta(seconds=60 * iteration)
print (iteration)
next_time_str = next_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
print(f"FINDING MENTIONS STARTING 1 MIN AGO AT {next_time}")


mentions = client.get_users_mentions('1663528031124701184', 
     max_results=5, 
    expansions=['author_id', 'referenced_tweets.id'])
    # since_id=1709870022997241907)
    # start_time=next_time_str)


# Check if there are no mentions
# if mentions is None or not mentions.data:
#     print("No new mentions.")
#     time.sleep(60)
#     # start_time += timedelta(seconds=60)
#     # continue  # Skip the rest of the loop and start the next iteration



for mention in mentions.data: 
        author_id = mention.author_id 
        author = next((user for user in mentions.includes['users'] if user.id == author_id), None)


# If there are mentions, iterate through them
alpha_testers = [1468881882167185408, 1468881882167185409, 1468881882167185401]

filtered_mentions = []
for mention in mentions.data:
    if mention['author_id'] in alpha_testers:
        filtered_mentions.append(mention)
    if not filtered_mentions:
        print("No mentions found for the specified author IDs.")


# filtered_mentions = [mention for mention in mentions.data if mention['author_id'] in alpha_testers]


# print (filtered_mentions)

for mention in filtered_mentions:
    referenced_tweets = mention.data['referenced_tweets']
    for referenced_tweet in referenced_tweets:
        referenced_tweet_id = referenced_tweet['id']

    saved_tweet = client.get_users_tweets(referenced_tweet_id, expansions=['author_id'])


# for mention in filtered_mentions:  # Assuming mentions have a 'data' attribute containing the list of mention objects
#         user_id = mention.id
#         tweet_id = mention.id
#         author_id = mention.author_id
#         author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
#     if author:
#         screen_name = author.username
        # reply_text = f"@{screen_name} Tweet saved forever!\n\nWill be verifiable on the blockchain -> {mint_link}"
        # reply_text = f"@{screen_name} Here's your tweet screenshot!"

        # client.create_tweet(text=reply_text, media_ids=[media_id], in_reply_to_tweet_id=tweet_id)
        # print(reply_text)



        # print(f"Referenced tweet ID: {referenced_tweet_id}")
        #Referenced tweet ID: 1709915703464079398 --> this the id of the tweet the mention replied to

    # print (mentions)
    # Response(data=[
        # <Tweet id=1710098666684612968 text='@WhaleChart @sayver_cc'>,     # --> this is the id of the mention
        # <Tweet id=1710097499040645368 text='@WhaleChart @sayver_cc'>],    # --> this is the id of the mention
        #     includes={'users': [<User id=1468881882167185408 name=Hunch username=hunch_nft>],     --> this is the id of users who tagged @sayver_cc
        #                 'tweets': 
        #                 [<Tweet id=1709870022997241907 text='JUST IN:\n\nSam Bankman-Fried’s college roommate testifies against him'>,  --> this is the id and text of ss

        #                 <Tweet id=1709915703464079398 text='JUST IN:\n\nRobert F. Kennedy vows to end of ‘White House war on Bitcoin’ if elected President'>]}, 

        #                 errors=[], meta={'result_count': 2, 'newest_id': '1710098666684612968', 'oldest_id': '1710097499040645368'})

 
# for mention in filtered_mentions:  # Assuming mentions have a 'data' attribute containing the list of mention objects
#     user_id = mention.id #error
#     tweet_id = mention.id
#     tweet_text = mention.text
#     author_id = mention.author_id 
#     author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
# if author:
#     screen_name = author.username
    # reply_text = f"@{screen_name} Tweet saved forever! Verify on the blockchain -> {mint_link}" 

    # # print (f"this is user id {user.id}") #error
    # print (f"this is mention id {tweet_id}") 
    # # print (f"this is {mention.author.id}")  #error
    # print (f"this is mention text {tweet_text}") 
    # # print (author.username) #handle of the user who mentioned
    # print (mention.author_id) 
    # print (author)  #handle of the user who mentioned



# id = tweet id of the tweet replied to
# text = actual text of the tweet replied to


# Response(data=[
#     <Tweet id=1710098666684612968 text='@WhaleChart @sayver_cc'>, 
#     <Tweet id=1710097499040645368 text='@WhaleChart @sayver_cc'>, 
#     <Tweet id=1709846688943550904 text='@elonmusk @sayver_cc'>, 
#     <Tweet id=1709838434888785960 text='@WhaleChart @sayver_cc'>, 
#     <Tweet id=1709837796285005975 text='@CryptoVonDoom @sayver_cc save tweet'>], 
#         includes={
#             'users': [<User id=1468881882167185408 name=Hunch username=hunch_nft>], 
#             'tweets': [<Tweet id=1709870022997241907 
#                 text='JUST IN:\n\nSam Bankman-Fried’s college roommate testifies against him'>, 

#         <Tweet id=1709915703464079398 text='JUST IN:\n\nRobert F. Kennedy vows to end of ‘White House war on Bitcoin’ if elected President'>, 
#         <Tweet id=1707864159784927270 text='Newspapers basically just report on what they read yesterday on X lmao'>, 
#         <Tweet id=1709532325946519596 text='JUST IN:\n\nBank of Korea announces plan to test wholesale CBDC'>, 
#         <Tweet id=1709835289412227384 text='Champagne for my real friends, real pain for my sham friends.'>]}, errors=[], meta={'result_count': 5, 'newest_id': '1710098666684612968', 'oldest_id': '1709837796285005975', 'next_token': '7140dibdnow9c7btw4803urdejdyhfsc5ao6la0l6ss39'})


# Response(data=[<Twee




