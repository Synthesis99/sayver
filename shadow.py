from shadow_drive import ShadowDriveClient
from solders.keypair import Keypair
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--keypair', metavar='keypair', type=str, required=True,
                    help='The keypair file to use (e.g. keypair.json, dev.json)')
args = parser.parse_args()

# Initialize client
client = ShadowDriveClient(args.keypair)
print("Initialized client")

# Create account
size = 2 ** 20
account, tx = client.create_account("sayver_alpha", size, use_account=True)
print(f"Created storage account {account}")