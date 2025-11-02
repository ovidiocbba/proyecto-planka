import requests
import pytest
import jsonschema
from config import  BASE_URI , TOKEN_INVALID , ID_BOARD2
from src.assertions.status_code import assert_status_code_200, assert_status_code_401
from src.resources.schemas.project_schema import SCHEMA_BOARD_OUTPUT2
from src.assertions.assertion_general import assert_response_time

@pytest.mark.board
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC013_get_board_with_valid_token(get_token):
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC014_get_board_with_invalid_token():
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }
    response = requests.get(url, headers=headers)
    assert_status_code_401(response)

@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.schema_validation
def test_TC015_validate_board_response_schema(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.get(url,headers=headers)
    assert_status_code_200(response)

    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_BOARD_OUTPUT2)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")

   
@pytest.mark.board
@pytest.mark.smoke
@pytest.mark.response_time
def test_TC016_validate_board_response_time(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_response_time(response)



