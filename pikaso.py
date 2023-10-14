
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
initial_run = datetime.now(timezone.utc) - timedelta(seconds=120)
print(f"INITIAL RUN STARTED AT {initial_run}")


while True:
    
    iteration += 1
    print (iteration)

    start = initial_run + timedelta(seconds=60 * iteration)
    end = start + timedelta(seconds=60)
    
    start_str = start.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    end_str = end.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    print(f"FINDING MENTIONS FROM {start} TO {end}")


    mentions = client.get_users_mentions('1230791624898146304', #pikaso_me ID
        max_results=5, 
        expansions=['author_id', 'referenced_tweets.id'], 
        start_time=start_str,
        end_time=end_str)


    # Check if there are no mentions
    if mentions is None or not mentions.data:
        print("No new mentions.")
        time.sleep(60)
        continue  # Skip the rest of the loop and start the next iteration

    for mention in mentions.data:  # Assuming mentions have a 'data' attribute containing the list of mention objects
            user_id = mention.id
            tweet_id = mention.id
            author_id = mention.author_id
            author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
    if author:
        screen_name = author.username

    requested_tweet = mentions.includes['tweets'][0]['text']
    # # print(requested_tweet)

    # # if "https://" in requested_tweet[-25:]:
    # #     # print("tweet not yet supported in alpha testing")
    # #     reply_reject = "Sorry, this type of tweet is not yet supported in alpha testing."
    # #     client.create_tweet(text=reply_reject, in_reply_to_tweet_id=tweet_id)
    # #     print(reply_reject)
    # #     continue
    # #     # time.sleep(60)
    # #     # continue  # Skip the rest of the loop and start the next iteration


    # for mention in mentions.data:
    #     referenced_tweets = mention.data['referenced_tweets']
    #     for referenced_tweet in referenced_tweets:
    #         referenced_tweet_id = referenced_tweet['id']

    #         saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id'], tweet_fields=['created_at'])

    #         # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id', ''])
    #         print(type(saved_tweet))
    #         print(saved_tweet)

    #         created_at = saved_tweet[0]['created_at']
    #         print(created_at)


    
    #         # # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id', ''], tweet_field=['created_at', ''])
    #         # saved_tweet = client.get_tweet(referenced_tweet_id, expansions=['author_id', ''])

    #         for tweet in saved_tweet:
    #             if isinstance(tweet, dict) and 'users' in tweet:  # check if the entry is a dictionary and has a 'users' key
    #                 user = tweet['users'][0]  # assuming there's only one user per entry
    #                 creator_id = user['id']
    #                 creator_username = user['username']
    #                 # print("User ID:", user_id)
    #                 # print("Username:", username)

    #                 tweet_link = (f"https://twitter.com/{creator_username}/status/{referenced_tweet_id}")
    #                 print(f"Found a new request! Saving {tweet_link}")
    #                 time.sleep(60)






    # # # Define whitelisted user ids
    # # alpha_testers = [1468881882167185408, 1663528031124701184]

    # # # Target author on mentions
    # # for mention in mentions.data: 
    # #     author_id = mention.author_id 
    # #     author = next((user for user in mentions.includes['users'] if user.id == author_id), None)

    # # filtered_mentions = [mention for mention in mentions.data if mention['author_id'] in alpha_testers]

    # # if not filtered_mentions:
    # #     print("No mentions found for the specified author IDs.")
    # #     time.sleep(50)
    # #     continue  # Skip the rest of the loop and start the next iteration        

    # # for mention in filtered_mentions:
    # #     referenced_tweets = mention.data['referenced_tweets']
    # #     for referenced_tweet in referenced_tweets:
    # #         referenced_tweet_id = referenced_tweet['id']
    # #         tweet_link = (f"https://twitter.com/sayver_cc/status/{referenced_tweet_id}")
    # #         print(f"Found a new request! Saving {tweet_link}")
    # #         time.sleep(50)





    # # Define the screenshot path here using the tweet ID
    # screenshot_path = f"{referenced_tweet_id}.png"


    # def capture_tweet_screenshot(tweet_url, screenshot_path):

    #     #Set timezone to UTC
    #     os.environ['TZ'] = 'UTC'
        
    #     # Set up the webdriver
    #     options = ChromeOptions()
    #     options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    #     # options.add_argument("--window-size=1080x1920")  # Vertical monitor size
    #     options.add_argument("--window-size=1440x2560")  # Vertical monitor size

    #     # options.add_argument("--force-dark-mode")  # Enable dark mode
    #     # options.add_argument("--disable-features=DarkMode")  # Disable website's dark mode override
    #     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-dev-shm-usage')
    #     browser = None

    #     try:

    #         # Make sure to point to the location of your ChromeDriver if it's not in PATH
    #         browser = Chrome(options=options)
            
    #         # Open the tweet
    #         browser.get(tweet_url)
            
    #         # Wait for the tweet element using an explicit wait
    #         wait = WebDriverWait(browser, 90)  # wait for up to 60 seconds
    #         tweet = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "article")))

    #         # Capture screenshot of the element
    #         tweet.screenshot(screenshot_path)
            

    #     except Exception as e:
    #         print(f"Error: {e}")

    #     finally:
    #         if browser:
    #             browser.quit()

    # tweet_url = f"https://twitter.com/twitter/status/{referenced_tweet_id}"
    # capture_tweet_screenshot(tweet_url, screenshot_path)


    # # Open the existing image
    # image_path = screenshot_path  # Replace with your image file's path
    # img = Image.open(image_path)

    # # Define the cropping coordinates (left, upper, right, lower)
    # left = 0   # X-coordinate of the left edge of the cropping box
    # upper = 0   # Y-coordinate of the upper edge of the cropping box
    # right = img.width  # X-coordinate of the right edge of the cropping box
    # lower = img.height - 88  # Y-coordinate of the lower edge of the cropping box

    # # Crop the image
    # cropped_img = img.crop((left, upper, right, lower))

    # # Save the cropped image
    # cropped_img.save(screenshot_path)  # Replace with your desired output file name and format

    # # # FROM UPLOAD.PY//////////////////////////////////////////////

    # subprocess.run(["python3", "upload.py", "--keypair", "shdw-keypair.json", "-s", "2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6", "--screenshot-path", screenshot_path])




    # # # FROM MINT.PY//////////////////////////////////////////////

    # # result = subprocess.run(['python3', 'mint.py', "--screenshot-path", screenshot_path, "--tweet-link", tweet_link, "--author-id", str(author_id), "--screen-name", screen_name, "--requested-tweet", requested_tweet, "scr"], capture_output=True, text=True)

    # print (tweet_link)
    # print (creator_id)
    # print (creator_username)
    # print (requested_tweet)
    # print (created_at)

    # result = subprocess.run(['python3', 'mint.py', 
    #                     "--screenshot-path", str(screenshot_path), 
    #                     "--tweet-link", str(tweet_link), 
    #                     "--creator-id", str(creator_id), 
    #                     "--creator-username", str(creator_username), 
    #                     "--requested-tweet", str(requested_tweet),
    #                     "--created-at", str(created_at)], 
    #                    capture_output=True, text=True)


    # mint_address = result.stdout.strip()

    # print (f"Mint address: {mint_address}")
    # mint_link = (f"https://xray.helius.xyz/token/{mint_address}?network=devnet")


    # # FROM QR.PY//////////////////////////////////////////////

    # subprocess.run(["python3", "qr.py", "--screenshot-path", screenshot_path, "--mint", mint_address])

    # # parser = argparse.ArgumentParser()
    # # parser.add_argument('--keypair', metavar='keypair', type=str, required=True,
    # #                     help='The keypair file to use (e.g. keypair.json, dev.json)')
    # # args = parser.parse_args()

    # # # Initialize client // run with CLI: upload.py --keypair shdw-keypair.json -s 2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6
    # # client = ShadowDriveClient(args.keypair)
    # # print("Initialized client")


    # # Upload image using V1 API
    # media_id = api.media_upload(filename=screenshot_path).media_id_string


    # Iterate over each mention and reply with the uploaded photo
    for mention in mentions.data:  # Assuming mentions have a 'data' attribute containing the list of mention objects
        user_id = mention.id
        tweet_id = mention.id
        author_id = mention.author_id
        author = next((user for user in mentions.includes['users'] if user.id == author_id), None)
    if author:
        screen_name = author.username
        # reply_text = f"@{screen_name} Tweet saved forever!\n\nWill be verifiable on the blockchain -> {mint_link}"
        reply_text = f"@{screen_name} sayver_cc also saves tweets. Please give this a try!\n\n\n\n"

        # client.create_tweet(text=reply_text, media_ids=[media_id], in_reply_to_tweet_id=tweet_id)
        client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        print(reply_text)

    # os.remove(screenshot_path)
    # print (f"{screenshot_path} deleted!")  

