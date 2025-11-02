import requests
import json
import pytest
import jsonschema
from config import BASE_URI , TOKEN_INVALID , ID_LIST2 , ID_LIST_NOT_EXISTS , ID_LIST_EMPTY , ID_LIST_INVALID_STRING
from src.assertions.status_code import assert_status_code_200 ,assert_status_code_400 ,assert_status_code_401 , assert_status_code_404,assert_status_code_400_or_404
from src.resources.payloads.project_payloads import PAYLOAD_CREATE_CARD , PAYLOAD_CREATE_CARD_TYPE_EMPTY,PAYLOAD_CREATE_CARD_POSITION_EMPTY,PAYLOAD_CREATE_CARD_NAME_EMPTY,PAYLOAD_CREATE_CARD_TYPE_PROJECT,PAYLOAD_CREATE_CARD_TYPE_STORY , PAYLOAD_CREATE_CARD_TYPE_INVALID,PAYLOAD_CREATE_CARD_POSITION_INVALID,PAYLOAD_CREATE_CARD_NAME_INVALID,PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS
from src.resources.schemas.project_schema import SCHEMA_CARD_PAYLOAD_INPUT


@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC022_create_card_with_valid_token(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)
    

@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC023_create_card_with_invalid_token():
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)
    
@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC024_validate_card_creation_request_payload(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

    try:
        jsonschema.validate(PAYLOAD_CREATE_CARD, schema= SCHEMA_CARD_PAYLOAD_INPUT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")



@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC025_post_card_validate_attribute_with_type_project(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_PROJECT)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC026_post_card_validate_attribute_with_type_story(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_STORY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC027_post_card_validate_attribute_with_type_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC028_post_card_validate_attribute_with_type_invalid(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC029_post_card_validate_attribute_with_position_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.xfail(reason=" BUG004: La atributo position  permite entradas de cadena ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC030_post_card_validate_attribute_with_position_invalid_type(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC031_post_card_validate_attribute_with_position_value_negative(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.xfail(reason="BG005: El atributo position no tiene un valor limite de cantidad de digitos ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC032_post_card_validate_position_attribute_exceeding_digit(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC033_post_card_validate_attribute_with_name_empty(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

@pytest.mark.xfail(reason=" BUG006: La atributo name  permite entradas de valor numerico ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC034_post_card_validate_attribute_with_name_invalid(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST2}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_NAME_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC035_post_card_with_nonexistent_list_id(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST_NOT_EXISTS}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400_or_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC036_post_card_with_empty_list_id(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST_EMPTY}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC037_post_card_with_invalid_list_id(get_token):
    url = f"{BASE_URI}/lists/{ID_LIST_INVALID_STRING}/cards"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)