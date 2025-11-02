import requests
import json
import pytest
import jsonschema
from config import BASE_URI , ID_BOARD2 , TOKEN_INVALID ,ID_BOARD_NOT_EXISTS , ID_BOARD_EMPTY , ID_BOARD_INVALID_STRING
from src.assertions.status_code import assert_status_code_200 , assert_status_code_400,assert_status_code_401 , assert_status_code_404 , assert_status_code_400_or_404
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_LIST , PAYLOAD_CREATE_LIST_TYPE_ACTIVE , PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_CLOSED,PAYLOAD_CREATE_LIST_EMPTY_TYPE,PAYLOAD_CREATE_LIST_EMPTY_POSITION,PAYLOAD_CREATE_LIST_EMPTY_NAME,PAYLOAD_CREATE_LIST_INVALID_TYPE,PAYLOAD_CREATE_LIST_INVALID_POSITION ,PAYLOAD_CREATE_LIST_INVALID_NAME,PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS
from src.resources.schemas.project_schema import SCHEMA_CREATE_LIST_OUTPUT,SCHEMA_LIST_PAYLOAD_INPUT



@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC047_create_list_with_valid_token(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC048_create_list_with_invalid_token():
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC049_post_list_with_attribute_type_active(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_ACTIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC050_post_list_with_attribute_type_closed(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_CLOSED)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC051_post_list_attribute_with_type_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC052_post_list_attribute_with_type_invalid(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC053_post_list_attribute_with_position_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.xfail(reason=" BUG007: La atributo position  permite entradas de cadena ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC054_post_list_attribute_with_position_invalid(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC055_post_list_attribute_position_with_value_negative(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.xfail(reason=" BUG008: El atributo position no tiene un valor limite de cantidad de digitos  ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC056_post_list_with_position_value_exceeding(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC057_post_list_attribute_with_name_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG009: La atributo name permite entradas de valor numerico ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC058_post_list_attribute_with_name_invalid(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.schema_validation
def test_TC059_validate_list_creation_response_schema(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_CREATE_LIST_OUTPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.schema_validation

def test_TC060_validate_list_creation_request_payload(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD2}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(PAYLOAD_CREATE_LIST, schema= SCHEMA_LIST_PAYLOAD_INPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC061_post_list_with_id_board_not_exists(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD_NOT_EXISTS}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400_or_404(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC062_post_list_with_id_board_empty(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD_EMPTY}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_404(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC063_post_list_with_id_board_invalid(get_token):
    url = f"{BASE_URI}/boards/{ID_BOARD_INVALID_STRING}/lists"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)