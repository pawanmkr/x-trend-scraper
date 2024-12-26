import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import USER_INPUT_SELECTOR, PASSWORD_INPUT_SELECTOR, LOGGED_IN_INDICATOR_SELECTOR

def save_cookies(driver, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)
    print("Cookies saved.")

def load_cookies_if_available(driver, file_path):
    try:
        with open(file_path, "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies loaded.")
    except FileNotFoundError:
        print("No cookies file found.")

def is_logged_in(driver):
    """check if the user is logged in already by looking for a logged-in specific element."""
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGGED_IN_INDICATOR_SELECTOR))
        )
        return True
    except Exception:
        return False

def login_with_credentials(driver, username, password):
    try:
        driver.get("https://x.com/i/flow/login")

        # enter username
        username_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, USER_INPUT_SELECTOR))
        )
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)

        # enter password
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # wait for successful login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGGED_IN_INDICATOR_SELECTOR))
        )
        print("Login successful.")
    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise

def fetch_trending_tags(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="link"][data-testid="trend"]'))
    )
    trending_topics = driver.find_elements(By.CSS_SELECTOR, 'div[role="link"][data-testid="trend"]')
    hashtags = []

    for item in trending_topics:
        try:
            trend_text = item.find_element(By.CSS_SELECTOR, '.r-b88u0q').text
            if trend_text:
                hashtags.append(trend_text)
        except Exception as e:
            print(f"Error processing trend item: {e}")
            continue
    print(hashtags)
    return hashtags