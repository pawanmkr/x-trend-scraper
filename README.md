# x-trend-scraper

This project is a web scraper that fetches trending topics from a website using Selenium and stores the data in a MongoDB database. The results are accessible via a FastAPI web interface. The scraper runs the Selenium script and displays the fetched trending topics along with additional details.

## Features
- Scrapes trending topics using Selenium
- Stores results in MongoDB
- Displays the trends on a simple web interface powered by FastAPI
- Shows the IP address used for the query
- Returns the record as a JSON extract from MongoDB

## Prerequisites
Before you begin, ensure you have the following installed: 

- chrome-driver
  ```bash
  https://googlechromelabs.github.io/chrome-for-testing/#stable
  ```

## Setup Instructions

Follow these steps to set up the project:

1. Clone the repository:
```bash
git clone https://github.com/pawanmkr/x-trend-scraper.git
```
2. cd into root dir
```bash
cd x-trend-scraper
```

3. start the virtual environment

for windows 
```bash
python -m venv venv
venv\Scripts\activate
```

for mac & linux
```bash
python3 -m venv venv
source venv/bin/activate
```
5. install dependencies
```bash
pip install -r requirements.txt
```

6. start the application
```bash
uvicorn app:app --reload
```
