import requests
import json
import pytest
from config import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST , PAYLOAD_CREATE_LIST_TYPE_ACTIVE , PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_CLOSED,PAYLOAD_CREATE_LIST_EMPTY_TYPE,PAYLOAD_CREATE_LIST_EMPTY_POSITION,PAYLOAD_CREATE_LIST_EMPTY_NAME,PAYLOAD_CREATE_LIST_INVALID_TYPE,PAYLOAD_CREATE_LIST_INVALID_POSITION ,PAYLOAD_CREATE_LIST_INVALID_NAME,PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS
from src.resources.schemas.list_schema import SCHEMA_CREATE_LIST_OUTPUT,SCHEMA_LIST_PAYLOAD_INPUT
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas



@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_create_list_with_valid_token(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_create_list_with_invalid_token():
    url = EndpointPlanka.BASE_LISTS.value
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC003_post_list_with_attribute_type_active(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_ACTIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)




@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC004_post_list_with_attribute_type_closed(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_TYPE_CLOSED)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC005_post_list_attribute_with_type_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC006_post_list_attribute_with_type_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_TYPE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC007_post_list_attribute_with_position_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)
 


@pytest.mark.xfail(reason=" BUG009: La atributo position  permite entradas de cadena ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC008_post_list_attribute_with_position_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_POSITION)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC009_post_list_attribute_position_with_value_negative(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG010: El atributo position no tiene un valor limite de cantidad de digitos  ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC010_post_list_with_position_value_exceeding(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC011_post_list_attribute_with_name_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_EMPTY_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.xfail(reason=" BUG011: La atributo name permite entradas de valor numerico ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC012_post_list_attribute_with_name_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST_INVALID_NAME)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC013_validate_list_creation_response_schema(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_CREATE_LIST_OUTPUT)
   

@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC014_validate_list_creation_request_payload(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_LIST,SCHEMA_LIST_PAYLOAD_INPUT)

    


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC015_post_list_with_id_board_not_exists(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400_or_404(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC016_post_list_with_id_board_empty(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_EMPTY.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_404(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC017_post_list_with_id_board_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_INVALID.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)
    