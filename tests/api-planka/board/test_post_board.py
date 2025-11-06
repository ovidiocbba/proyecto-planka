import requests
import json
import jsonschema
import pytest
from config import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200 , assert_status_code_401, assert_status_code_400,assert_status_code_404,assert_status_code_400_or_404
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE , PAYLOAD_BOARD_EMPTY_NAME,PAYLOAD_BOARD_EMPTY_POSITION, PAYLOAD_BOARD_NAME_VALUE_NUMBER,PAYLOAD_BOARD_POSITION_NEGATIVE,PAYLOAD_BOARD_POSITION_INVALID_TYPE,PAYLOAD_BOARD_POSITION_LARGE
from src.resources.schemas.board_schema import SCHEMA_BOARD_OUTPUT

from utils.logger_helper import log_request_response

@pytest.mark.board
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_create_board_with_valid_token(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_200(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation 
def test_TC002_create_board_with_invalid_token():
    url = EndpointPlanka.BASE_BOARDS.value
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC003_create_board_with_empty_name(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_EMPTY_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG001: El atributo name  permite entradas de valor numerico ",run=True)
@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC004_create_board_with_numeric_name(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_NAME_VALUE_NUMBER)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_404(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC005_create_board_with_empty_position(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_EMPTY_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC006_create_board_with_negative_position(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_POSITION_NEGATIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG002: El atributo position  permite entradas de valor cadena ",run=True)
@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC007_create_board_with_invalid_position_type(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_POSITION_INVALID_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_404(response)



@pytest.mark.xfail(reason=" BUG003: El atributo position no tiene un valor limite de cantidad de digitos ",run=True)
@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
def test_TC008_create_board_with_position_attribute_exceeding_digit(get_token):
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_POSITION_LARGE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC009_validate_board_response_schema(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS.value
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)

    assert_status_code_200(response)
    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_BOARD_OUTPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")

    

@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC010_post_board_with_nonexistent_project_id(get_token):
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400_or_404(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC011_post_board_with_empty_project_id(get_token):
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_EMPTY.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_404(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC012_post_board_with_invalid_project_id_type(get_token):
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_INVALID.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_BOARD_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}',
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    assert_status_code_400(response)

