import uuid
import requests

def generate_unique_id():
    return str(uuid.uuid4())

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        print(f"Error fetching IP address: {e}")
        return "Unknown"