from dotenv import load_dotenv
load_dotenv()


import requests
import os

url = "https://devnet.underdogprotocol.com/v2/projects"

payload = {
    "attributes": { "stage": "beta" },
    "name": "Sayver Beta",
    "image": "https://shdw-drive.genesysgo.net/5p14ebgYub3zkC75dDmyF3EvwiV5NzYE4QwhgKSaTGY4/sayver.png",
    "semifungible": False,
    "isPublic": True,
    "externalUrl": "https://x.com/sayver_cc",
    "description": "Beta Testing - Devnet"
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

print(response.text)