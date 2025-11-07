import requests
import json
import pytest
from config import BASE_URI , ID_PROJECT1
from src.routes.endpoint import EndpointPlanka
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE 
from utils.logger_helper import get_logger

logger = get_logger("board_fixture")

@pytest.fixture(scope="function")
def post_test_board(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    board_id = data["item"]["id"]
    yield board_id
   
   

@pytest.fixture(scope="module")
def setup_add_board(get_token):
    created_boards = []
    logger.info("Setup iniciado para creación de tableros")
    yield get_token,created_boards

    logger.info("Iniciando teardown de tableros creados")
    for board in created_boards:
        board_id = board.get("item", {}).get("id")
        try:
              delete_url = f"{BASE_URI}/boards/{board_id}"
              headers = {
                    'Authorization': f'Bearer {get_token}'
                } 
              delete_response = requests.delete(delete_url,headers=headers)
              if delete_response.status_code == 200:
                    logger.info(f"Tablero eliminado correctamente: {board_id}")
              else:
                   logger.error(f" No se pudo eliminar el tablero {board_id}. ")
        except Exception as e:
          logger.exception(f"Error eliminando tablero: {e}")