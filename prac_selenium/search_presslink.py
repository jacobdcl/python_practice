from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# set path to webdriver executable
webdriver_path = '/Users/jacoblurker/chromedriver'

# initialize the driver using Service
service = Service(webdriver_path)

try:
    driver = webdriver.Chrome(service=service)
    # Open a webpage
    driver.get('https://www.google.com')
    # keep browser window open for 10 seconds
    time.sleep(22)
except Exception as e:
    print(f"An exception occurred: {e}")
finally:
    # Close the browser
    driver.quit()
