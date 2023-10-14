
import cv2
import numpy as np
from PIL import Image
import os
import argparse
import segno
import pyshorteners
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--screenshot-path', metavar='screenshot_path', type=str, required=True,
                     help='The path to the screenshot file')
parser.add_argument('--mint', metavar='mint_address', type=str, required=True,
                    help='Mint address')
args = parser.parse_args()

screenshot_path = args.screenshot_path
mint_address = args.mint

s = pyshorteners.Shortener()


# Construct the mint link
mint_link = (f"https://xray.helius.xyz/token/{mint_address}?network=devnet") 

response = requests.get(f"https://is.gd/create.php?format=simple&url={mint_link}")

if response.status_code == 200:
    shortened_url = response.text.strip()
    print("Shortened URL:", shortened_url)
else:
    print("Failed to shorten URL. Status code:", response.status_code)

print("Mint Link:", shortened_url)

# Create and save QR code
qrcode = segno.make_qr(shortened_url, error='Q')
    
# Save the QR code image
qrcode.save(f"qr_{screenshot_path}", scale=3, border=1, light="yellow")

# Load images with PIL
bg_image = Image.open(screenshot_path)
overlay_image = Image.open(f"qr_{screenshot_path}")

# Resize overlay image to your desired size
qrcode_size = 50
overlay_image = overlay_image.resize((qrcode_size, qrcode_size))

# Calculate overlay image size
overlay_width, overlay_height = overlay_image.size

# Calculate the position for upper right corner
bg_width, bg_height = bg_image.size
position = (bg_width - overlay_width, 0)  # Upper right corner
bg_image.paste(overlay_image, position)  # Overlay the QR code onto the background image

# Save the resulting image
bg_image.save(screenshot_path)

# Clean up by removing the temporary QR code image
os.remove(f"qr_{screenshot_path}")
