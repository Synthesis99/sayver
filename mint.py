import requests
import argparse
import os
import json

parser = argparse.ArgumentParser()

url = "https://devnet.underdogprotocol.com/v2/projects/4/nfts"

parser.add_argument('--screenshot-path', metavar='screenshot_path', type=str, required=True,
                    help='The path to the screenshot file')
parser.add_argument('--tweet-link', metavar='tweet_link', type=str, required=True,
                    help='Link to tweet')
parser.add_argument('--creator-id', metavar='creator_id', type=str, required=True,
                    help='Twitter ID of creator')
parser.add_argument('--creator-username', metavar='creator_username', type=str, required=True,
                    help='Twitter handle of creator')
parser.add_argument('--requested-tweet', metavar='requested_tweet', type=str, required=True,
                    help='Content of tweet')
parser.add_argument('--created-at', metavar='created_at', type=str, required=True,
                    help='Date and time the tweet was created (UTC)')

args = parser.parse_args()

screenshot_path = args.screenshot_path
tweet_link = args.tweet_link
creator_id = args.creator_id
creator_username = args.creator_username
requested_tweet = args.requested_tweet
created_at = args.created_at

uploaded_file = f"https://shdw-drive.genesysgo.net/2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6/{screenshot_path}"

payload = {
    "receiverAddress": "SaYVDPuigHRyVmZ783TcCEDXdCCvH4gu7WTpJec4meW", 
    "delegated": True,       
    "attributes": {
        "launch type": "beta",
        "type": "tweet",
        "source": tweet_link, #link to tweet
        "creator id": creator_id, #user id
        "creator username": f"@{creator_username}", #twitter handle
        "content": requested_tweet, #tweet text
        "created at (UTC)": created_at #time and date tweet was created
        # "date saved":  #date minted

    },
    "name": screenshot_path,
    "image": uploaded_file
}

underdog_bearer_token = os.environ.get('UNDERDOG_BEARER_TOKEN')
if not underdog_bearer_token:
    raise ValueError("Bearer token is not set!")

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {underdog_bearer_token}"
}

response = requests.post(url, json=payload, headers=headers)

response_data = response.json()


# mint_address = response_data['mintAddress']
# print (mint_address)

projectId = int(response_data['projectId'])
nftId = int(response_data['nftId'])
# print(projectId)
# print(nftId)


url = (f"https://devnet.underdogprotocol.com/v2/projects/{projectId}/nfts/{nftId}")

underdog_bearer_token = os.environ.get('UNDERDOG_BEARER_TOKEN')
if not underdog_bearer_token:
    raise ValueError("Bearer token is not set!")

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {underdog_bearer_token}"
}

response2 = requests.get(url, headers=headers)
response2_data = response2.json()
response2 = requests.get(url, headers=headers)

# print(response2.text)


# Parse the JSON response from response.text
response2_data = json.loads(response2.text)


# Extract and print the mintAddress from the parsed JSON
mint_address = response2_data.get('mintAddress')
print(mint_address)