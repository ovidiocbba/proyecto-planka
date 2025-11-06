import pytest
import requests
import json
from config import BASE_URI, USER_EMAIL, USER_PASSWORD




@pytest.fixture(scope="session")
def get_token():
    url = f"{BASE_URI}/access-tokens"
    payload = json.dumps({
    "emailOrUsername": USER_EMAIL,
    "password": USER_PASSWORD

    })
    headers = {
    'Content-Type': 'application/json'
   }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    access_token = response_json['item']
    
    return access_token








    