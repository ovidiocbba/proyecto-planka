import pytest
import requests
import json
from config import BASE_URI
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST
from src.routes.endpoint import EndpointPlanka
from utils.logger_helper import get_logger

logger = get_logger("list_fixture")


@pytest.fixture(scope="function")
def create_test_list(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)

    data = response.json()
    list_id = data["item"]["id"]
    yield list_id
   
    



@pytest.fixture(scope="module")
def setup_add_list(get_token):
    created_lists = []      
    logger.info("Setup iniciado para creación de listas")
    yield get_token,created_lists


    logger.info("Iniciando teardown de listas creados")
    for list in created_lists:
        list_id = list.get("item", {}).get("id")
        try:
            delete_url = f"{BASE_URI}/lists/{list_id}"
            headers = {
                    'Authorization': f'Bearer {get_token}'
                } 
            delete_response = requests.delete(delete_url,headers=headers)
            if delete_response.status_code == 200:
                     logger.info(f"Lista eliminado correctamente: {list_id}")
            else:
                    logger.error(f" No se pudo eliminar el lista {list_id}. ")
        except Exception as e:
            logger.exception(f"Error eliminando lista: {e}")  


