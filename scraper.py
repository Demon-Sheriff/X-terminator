from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# wait for login completion (max wait is 5 seconds)
time.sleep(4) # wait for 4 seconds (to update this one.)
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-175oi2r r-6koalj r-eqz5dr r-16y2uox r-1habvwh r-cnw61z r-13qz1uu r-1ny4l3l r-1loqt21")))
# after logging in navigate to the profile section of the user.


print("done")

# for _ in range(10):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#     time.sleep(2)

# followers = driver.find_elements(By.CSS_SELECTOR, "div[dir='ltr'] > span")

# for follower in followers:
#     print(follower.text)

driver.quit()