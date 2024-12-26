from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import undetected_chromedriver as uc
from selenium_utils import load_cookies_if_available, is_logged_in, login_with_credentials, fetch_trending_tags, \
    save_cookies
from utils import get_ip_address, generate_unique_id
from database import store_trending_data
import datetime

app = FastAPI()

# Setup the Jinja2 template engine
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/run_script", response_class=JSONResponse)
async def run_script():
    driver = uc.Chrome()
    cookies_file = "cookies.pkl"
    trending_tags = []
    ip_address = get_ip_address()
    unique_id = generate_unique_id()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        driver.get("https://x.com/")
        # Load cookies if available
        load_cookies_if_available(driver, cookies_file)
        driver.refresh()

        if not is_logged_in(driver):
            print("session expired or not logged in. logging in...")
            login_with_credentials(driver, "Josh65430646916", "Tinker@c0de")
            save_cookies(driver, cookies_file)
        else:
            print("session is active. Bo login required.")

        # Fetch trending tags
        trending_tags = fetch_trending_tags(driver)

        store_trending_data(trending_tags, unique_id, ip_address)

    except Exception as e:
        print(f"an error occurred: {e}")
    finally:
        driver.quit()

    # Return the result as JSON to display in HTML
    return JSONResponse({
        "timestamp": timestamp,
        "trending_tags": trending_tags,
        "ip_address": ip_address,
        "unique_id": unique_id
    })