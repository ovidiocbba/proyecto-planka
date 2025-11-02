import requests
import json
import pytest
from config import BASE_URI, ID_LIST2
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_CARD


@pytest.fixture(scope="module")
def post_card(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    card_id = data["item"]["id"]
    yield card_id
   
    delete_url = f"{BASE_URI}/cards/{card_id}"
    delete_response = requests.delete(delete_url,headers=headers)
    if delete_response.status_code != 200:
        print(f"Teardown: no se pudo borrar el proyecto {card_id}: {delete_response.text}")