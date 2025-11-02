import requests
import json
import pytest
from config import BASE_URI , ID_PROJECT1
from src.assertions.status_code import assert_status_code_200 
from src.resources.payloads.project_payloads import PAYLOAD_BOARD_CREATE 


@pytest.fixture(scope="module")
def post_test_board(get_token):
    url = f"{BASE_URI}/projects/{ID_PROJECT1}/boards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    board_id = data["item"]["id"]
    yield board_id
   
    delete_url = f"{BASE_URI}/projects/{ID_PROJECT1}"
    delete_response = requests.delete(delete_url,headers=headers)
    if delete_response.status_code != 200:
             print(f"Teardown: no se pudo borrar el tablero {board_id}: {delete_response.text}")

