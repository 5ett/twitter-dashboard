import os
import requests
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('MY_BEARER_TOKEN')

new_endpoint = "https://api.twitter.com/2/tweets/counts/recent"

query_params = {'query': f'from:sanzenkuro', 'granularity': 'day'}

bearer_token = os.getenv('MY_BEARER_TOKEN')

def bearer_oauth(r):
    r.headers["Authorization"] = f'Bearer {bearer_token}'
    r.headers["User-Agent"] = "roobotDash"
    return r

def connect_to_endpoint(url, tweet_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=tweet_fields)
    print (response.status_code)

    if response.status_code != 200:
        raise Exception(f"there was a {response.status_code} error: {response.text}")
    
    return response.json()

json_response = connect_to_endpoint(new_endpoint, query_params)

colors = { "background": "#FFFFFF", "text":"#1DA1F2" }