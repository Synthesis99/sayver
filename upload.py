from shadow_drive import ShadowDriveClient
from solders.keypair import Keypair
from urllib.parse import quote
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--keypair', metavar='keypair', type=str, required=True,
                    help='The keypair file to use (e.g. keypair.json, dev.json)')
parser.add_argument('-s', metavar='account_id', type=str, required=True,
                    help='The account ID to use')
parser.add_argument('--screenshot-path', metavar='screenshot_path', type=str, required=True,
                    help='The path to the screenshot file')
args = parser.parse_args()

screenshot_path = args.screenshot_path


# Initialize client // run with CLI: upload.py --keypair shdw-keypair.json -s 2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6
client = ShadowDriveClient(args.keypair)
print("Initialized client")

# # Create account
# size = 2 ** 20
# account, tx = client.create_account("full_test", size, use_account=True)
# print(f"Created storage account {account}")
# // Created storage account 2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6
# // Created storage account GTxXoDPSsRzcDmL3pqeWv1UQ34F26cbzW4JPmMcj7Lv1

# # Upload files
client.set_account('2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6')
# files = ["sayver.png"]
# urls = client.upload_files(files)
# print("Uploaded file to https://shdw-drive.genesysgo.net/2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6/temp_screenshot1.png")

# client.set_account('2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6')
files = [screenshot_path]
urls = client.upload_files(files)
print(f"Uploaded file to https://shdw-drive.genesysgo.net/2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6/{screenshot_path}")

# # Add and Reduce Storage
# client.add_storage(2**20)
# client.reduce_storage(2**20)

# # Get file
# current_files = client.list_files()
# file = client.get_file(current_files[0])
# print(f"got file {file}")

# Delete files
# urls = ['https://shdw-drive.genesysgo.net/2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6/sayver%20logo.png']
# client.delete_files(urls)
# print("Deleted files")

# # Delete account
# client.delete_account(account)
# print("Closed account")