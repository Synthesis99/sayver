import os
import requests
import zipfile


def check_driver():
    url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win32/chrome-win32.zip"
    if not os.path.exists("binaries"):
        print("Downloading Driver...")
        os.makedirs("binaries")
        response = requests.get(url)
        zip_path = os.path.join("binaries", "chromedriver.zip")
        with open(zip_path, "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("binaries")
        print("Driver Downloaded Successfully!")
