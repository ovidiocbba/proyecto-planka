import pytest
from src.routes.request import PlankaRequests
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE
from src.routes.endpoint import EndpointPlanka
from utils.config import BASE_URI, USER_EMAIL, USER_PASSWORD
from utils.logger_helper import get_logger


logger = get_logger("fixture")

@pytest.fixture(scope="session")
def get_token():
    url = f"{BASE_URI}/access-tokens"
    payload = {
            "emailOrUsername": USER_EMAIL,
            "password": USER_PASSWORD
    }
    headers = {'Content-Type': 'application/json'}
    response = PlankaRequests.post(url, headers, payload)
    response_json = response.json()
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    access_token = response_json['item']
    return access_token


@pytest.fixture(scope="module")
def id_project(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
      response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
      data = response.json()
      project_id = data["item"]["id"]
      logger.info("Setup iniciado para creación de proyectos")
      return project_id


@pytest.fixture(scope="module")
def id_board(get_token,id_project):
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards" 
    TOKEN_PLANKA = get_token
    payload = PAYLOAD_BOARD_CREATE
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}',}
    response = PlankaRequests.post(url,headers,payload)
    data = response.json()
    board_id = data["item"]["id"]
    return board_id



@pytest.fixture(scope="module")
def id_list(get_token,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"  
    TOKEN_PLANKA = get_token
    payload = PAYLOAD_CREATE_LIST
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,payload)
    data = response.json()
    list_id = data["item"]["id"]
    return list_id
    
    
@pytest.fixture(scope="module")
def id_card(get_token,id_list):
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    TOKEN_PLANKA = get_token
    payload = PAYLOAD_CREATE_CARD
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url, headers, payload)
    data = response.json()
    card_id = data["item"]["id"]
    return card_id















