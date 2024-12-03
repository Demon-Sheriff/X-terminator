from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os, dotenv

TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"

dotenv.load_dotenv()
options = Options()
options.binary_location = '/usr/bin/brave-browser'
# driver_path = 

# logging into twitter
driver = webdriver.Chrome(options=options)

driver.maximize_window() # maximise the window
driver.get(TWITTER_LOGIN_URL)
time.sleep(2)

# input the username
# username = driver.find_element('xpath', "//input[@autocomplete='username']")
username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
print("this is done")
username.send_keys("prompt_Tunes")
username.send_keys(Keys.RETURN)
time.sleep(2)

# input the password
password = driver.find_element("xpath", "//input[@autocomplete='current-password']")
password.send_keys(os.getenv("PASSWORD"))
password.send_keys(Keys.RETURN)
time.sleep(4)

print("done")

# for _ in range(10):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#     time.sleep(2)

# followers = driver.find_elements(By.CSS_SELECTOR, "div[dir='ltr'] > span")

# for follower in followers:
#     print(follower.text)

driver.quit()