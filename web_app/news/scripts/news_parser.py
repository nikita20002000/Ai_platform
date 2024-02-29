import requests
from dotenv import load_dotenv
import os
load_dotenv()
import json

API_KEY = os.getenv('VITE_NEWS_API_KEY')

def get_news(API_KEY=API_KEY, keyword='Business'):
    url = (f'https://api.currentsapi.services/v1/search?keywords={keyword}&language=en&language=us&'
           f'apiKey={API_KEY}')

    response = requests.get(url)
    return (response.json())

