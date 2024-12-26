from pymongo import MongoClient
import datetime


def get_db():
    # env's should always be used safely but for the sake of assignment showcase i have used directly here
    # to avaid hassle of setting up everything
    client = MongoClient(
        "mongodb+srv://pawan:mintmint@automail.kfm6mu6.mongodb.net/?retryWrites=true&w=majority&appName=automail")
    db = client['selenium_data']
    return db


def store_trending_data(trending_tags, unique_id, ip_address):
    db = get_db()
    collection = db.trending_data

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "unique_id": unique_id,
        "timestamp": timestamp,
        "ip_address": ip_address,
        "trending_tags": trending_tags
    }
    result = collection.insert_one(data)

    return result.inserted_id