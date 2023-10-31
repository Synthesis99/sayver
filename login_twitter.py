import os
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from check_driver import check_driver

check_driver()
# Set timezone to UTC
os.environ["TZ"] = "UTC"

# Set up the webdriver
options = ChromeOptions()
tweet_url = "https://twitter.com/"
# options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
# options.add_argument("--window-size=1080x1920")  # Vertical monitor size
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--window-size=1440x2560")  # Vertical monitor size
options.add_argument("--user-data-dir=selenium_session")
# os.chmod('selenium_session', 0o777)


# options.add_argument("--force-dark-mode")  # Enable dark mode
# options.add_argument("--disable-features=DarkMode")  # Disable website's dark mode override
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "binaries\chrome-win32\chrome.exe"
browser = None

# Make sure to point to the location of your ChromeDriver if it's not in PATH
browser = Chrome(options=options)
browser.maximize_window
# browser.execute_script("document.body.style.zoom='100%'")
# Open the tweet
browser.get(tweet_url)
time.sleep(99999)
