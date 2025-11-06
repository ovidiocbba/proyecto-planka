import requests
import json
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200 
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE 
from utils.logger_helper import log_request_response




@pytest.mark.board
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
def test_create_board(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers,payload)
    assert_status_code_200(response)


@pytest.mark.board
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_get_board_by_id(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)


@pytest.mark.board
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_delete_board_by_id(get_token,post_test_board):
    TOKEN_PLANKA = get_token
    ID_BOARD =  post_test_board
    url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{ID_BOARD}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)