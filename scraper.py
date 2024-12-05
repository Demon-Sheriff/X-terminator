from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, dotenv

TWITTER_LOGIN_URL = "https://x.com/prompt_Tunes/"
FOLLOWERS_PAGE = "https://x.com/prompt_Tunes/followers"

dotenv.load_dotenv()
options = Options()
options.binary_location = '/usr/bin/brave-browser'
# driver_path = 

# logging into twitter
driver = webdriver.Chrome(options=options)

driver.maximize_window() # maximise the window
driver.get(TWITTER_LOGIN_URL)
# time.sleep(4)

# wait for the visibility of username input field
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
print("me is done")
# input the username
# username = driver.find_element('xpath', "//input[@autocomplete='username']")
username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
print("this is done")
username.send_keys("prompt_Tunes")
username.send_keys(Keys.RETURN)
# time.sleep(4)

# input the password
password = None
try:
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    # Send input to the password field
    password.send_keys(os.getenv("PASSWORD"))
    password.send_keys(Keys.RETURN)
    print("Password input field found and interacted with!")
except Exception as e:
    print("Error locating the password input field:", e)
# password = driver.find_element(By.NAME, "password")
# password = driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
# wait for the visibility of the password input field.
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
# password.send_keys(os.getenv("PASSWORD"))
# password.send_keys(Keys.RETURN)
time.sleep(4)

# wait for login completion (max wait is 5 seconds)
time.sleep(4) # wait for 4 seconds (to update this one.)
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-175oi2r r-6koalj r-eqz5dr r-16y2uox r-1habvwh r-cnw61z r-13qz1uu r-1ny4l3l r-1loqt21")))
# after logging in navigate to the profile section of the user.


print("done")



# wait until the login procedure is completed.
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="css-175oi2r r-sdzlij r-dnmrzs r-1awozwy r-18u37iz r-1777fci r-xyw6el r-o7ynqc r-6416eg"]')))

print("hitting the followers URL after logging in")
driver.get(FOLLOWERS_PAGE)


# for _ in range(10):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#     time.sleep(2)

# followers = driver.find_elements(By.CSS_SELECTOR, "div[dir='ltr'] > span")

# for follower in followers:
#     print(follower.text)

driver.quit()