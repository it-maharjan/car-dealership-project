# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

import requests
from urllib.parse import urlencode

def get_request(endpoint, **kwargs):
    try:
        # Encode the parameters safely
        params = urlencode(kwargs) if kwargs else ""
        
        # Construct the full URL
        request_url = f"{backend_url}{endpoint}?{params}"
        
        print(f"GET from {request_url}")
        
        # Make the GET request
        response = requests.get(request_url)
        
        # Check if the response was successful
        if response.status_code == 200:
            return response.json()  # Parse JSON response
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    
    except requests.exceptions.RequestException as e:
        # Handle network exceptions
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
# Add code for posting review
