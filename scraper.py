from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, dotenv

TWITTER_LOGIN_URL = "https://x.com/prompt/"
FOLLOWERS_PAGE = "https://x.com/prompt/followers"

dotenv.load_dotenv()
options = Options()
options.binary_location = '/usr/bin/brave-browser'

# logging into twitter
driver = webdriver.Chrome(options=options)

driver.maximize_window() # maximise the window
driver.get(TWITTER_LOGIN_URL)
# time.sleep(4)

# wait for the visibility of username input field
username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
print("me is done")
# input the username
# username = driver.find_element('xpath', "//input[@autocomplete='username']")
# username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
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

print(f"fetching the followers data")

# followers = driver.find_elements(By.CSS_SELECTOR, "span.css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3")
# wait unitl the followers are visible
# followers = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")))
# followers = driver.find_elements(By.CSS_SELECTOR, "span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
# print(len(followers))

from selenium.common.exceptions import TimeoutException

try:
    followers = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div[data-testid='primaryColumn']  div.css-175oi2r > div.css-175oi2r.r-1awozwy.r-18u37iz.r-1wbh5a2 > div.css-175oi2r.r-1wbh5a2.r-dnmrzs > a.css-175oi2r.r-1wbh5a2.r-dnmrzs.r-1ny4l3l.r-1loqt21 > div.css-175oi2r > div.css-146c3p1.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-18u37iz.r-1wvb978 > span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
        )
    )
    for follower in followers:
        print(follower.text)
except TimeoutException:
    print("Followers not found within the given timeout period.")

driver.quit()
