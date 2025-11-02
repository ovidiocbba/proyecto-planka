import requests
import json
import jsonschema
import pytest
from config import BASE_URI , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200,assert_status_code_400,assert_status_code_401
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE , PAYLOAD_PROJECT_CREATE_NAME_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_SHARED,PAYLOAD_PROJECT_CREATE_TYPE_PRIVATE,PAYLOAD_PROJECT_CREATE_TYPE_INVALID,PAYLOAD_PROJECT_CREATE_NAME_NUMBER
from src.resources.schemas.project_schema import SCHEMA_OUTPUT_CREATE_PROJECT,SCHEMA_INPUT_CREATE_PROJECT


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC073_create_project_with_valid_token(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC074_create_project_with_invalid_token():
    url = f"{BASE_URI}/projects"
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }
     
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC075_validate_project_creation_response_payload(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token 
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


    try:
        jsonschema.validate(instance=response.json(), schema= SCHEMA_OUTPUT_CREATE_PROJECT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


@pytest.mark.project_management
@pytest.mark.payload_validation
@pytest.mark.functional_positive
def test_TC076_validate_project_creation_request_payload(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    headers = {
        'Authorization': f'Bearer {TOKEN_PLANKA}'
        }
    
    response = requests.post(url,headers=headers,json=PAYLOAD_PROJECT_CREATE)
    assert_status_code_200(response)


    try:
        jsonschema.validate(PAYLOAD_PROJECT_CREATE, schema= SCHEMA_INPUT_CREATE_PROJECT)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC077_create_project_with_attribute_type_private(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_PRIVATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC078_create_project_with_attribute_type_shared(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_SHARED)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC079_create_project_with_attribute_type_empty(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC080_create_project_with_attribute_type_invalid(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC081_create_project_with_attribute_name_empty(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)


@pytest.mark.xfail(reason=" BUG010: La atributo nombre del proyecto permite entradas numéricas ",run=True)
@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC082_create_project_with_attribute_name_value_number(get_token):
    url = f"{BASE_URI}/projects"
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_NAME_NUMBER)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_400(response)

