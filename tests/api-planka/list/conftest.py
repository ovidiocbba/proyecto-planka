import pytest
import requests
import json
from config import BASE_URI, ID_BOARD2
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_LIST


@pytest.fixture(scope="module")
def create_test_list(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)

    data = response.json()
    list_id = data["item"]["id"]
    yield list_id
   
    delete_url = f"{BASE_URI}/lists/{list_id}"
    delete_response = requests.delete(delete_url,headers=headers)
    if delete_response.status_code != 200:
        print(f"Teardown: no se pudo borrar el proyecto {list_id}: {delete_response.text}")