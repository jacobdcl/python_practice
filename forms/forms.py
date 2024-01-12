from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Set the path to the webdriver executable
webdriver_path = '/Users/jacoblurker/chromedriver'  # replace with your path

# Initialize the driver using Service
service = Service(webdriver_path)

try:
    driver = webdriver.Chrome(service=service)

    # Open a webpage
    driver.get('https://www.google.com')

    # Keep the browser window open for 10 seconds
    time.sleep(22)  # This will pause the execution and keep the browser open for 10 seconds
except Exception as e:
    print(f"An exception occurred: {e}")
finally:
    # Close the browser
    driver.quit()
