import requests
import json
import pytest
from config import TOKEN_INVALID 
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD , PAYLOAD_CREATE_CARD_TYPE_EMPTY,PAYLOAD_CREATE_CARD_POSITION_EMPTY,PAYLOAD_CREATE_CARD_NAME_EMPTY,PAYLOAD_CREATE_CARD_TYPE_PROJECT,PAYLOAD_CREATE_CARD_TYPE_STORY , PAYLOAD_CREATE_CARD_TYPE_INVALID,PAYLOAD_CREATE_CARD_POSITION_INVALID,PAYLOAD_CREATE_CARD_NAME_INVALID,PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS
from src.resources.schemas.card_schema import SCHEMA_CARD_PAYLOAD_INPUT
from src.routes.endpoint import EndpointPlanka
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas


@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_create_card_with_valid_token(setup_add_card):
    get_token,created_cards = setup_add_card
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_cards.append(response.json())

    
    

@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_create_card_with_invalid_token():
    url = EndpointPlanka.BASE_CARDS.value
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_401(response)

    



@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
def test_TC003_validate_card_creation_request_payload(setup_add_card):
    get_token,created_cards = setup_add_card
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_CARD, SCHEMA_CARD_PAYLOAD_INPUT)
    created_cards.append(response.json())


   

@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC004_post_card_validate_attribute_with_type_project(setup_add_card):
    get_token,created_cards = setup_add_card
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_PROJECT)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_cards.append(response.json())
    



@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC005_post_card_validate_attribute_with_type_story(setup_add_card):
    get_token,created_cards = setup_add_card
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_STORY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_cards.append(response.json())
    



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC006_post_card_validate_attribute_with_type_empty(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC007_post_card_validate_attribute_with_type_invalid(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_TYPE_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)
  


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC008_post_card_validate_attribute_with_position_empty(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)
  


@pytest.mark.xfail(reason=" BUG005: La atributo position  permite entradas de cadena ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC009_post_card_validate_attribute_with_position_invalid_type(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC010_post_card_validate_attribute_with_position_value_negative(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.xfail(reason="BG006: El atributo position no tiene un valor limite de cantidad de digitos ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC011_post_card_validate_position_attribute_exceeding_digit(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC012_post_card_validate_attribute_with_name_empty(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG007: La atributo name  permite entradas de valor numerico ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC013_post_card_validate_attribute_with_name_invalid(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD_NAME_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC014_post_card_with_nonexistent_list_id(get_token):
    url = EndpointPlanka.BASE_CARD_WITH_ID_LIST_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400_or_404(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC015_post_card_with_empty_list_id(get_token):
    url = EndpointPlanka.BASE_CARD_WITH_ID_LIST_EMPTY.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_404(response)



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC016_post_card_with_invalid_list_id(get_token):
    url = EndpointPlanka.BASE_CARD_WITH_ID_LIST_INVALID.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)
