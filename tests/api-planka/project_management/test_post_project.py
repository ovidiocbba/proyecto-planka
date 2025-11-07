import requests
import json
import pytest
from config import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE , PAYLOAD_PROJECT_CREATE_NAME_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_SHARED,PAYLOAD_PROJECT_CREATE_TYPE_PRIVATE,PAYLOAD_PROJECT_CREATE_TYPE_INVALID,PAYLOAD_PROJECT_CREATE_NAME_NUMBER
from src.resources.schemas.project_schema import SCHEMA_INPUT_CREATE_PROJECT,SCHEMA_OUTPUT_CREATE_PROJECT
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response



@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC001_create_project_with_valid_token(setup_add_project):
    url = EndpointPlanka.BASE_PROJECTS.value
    get_token , created_projects = setup_add_project
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {get_token}'
    }
    response = requests.post(url, headers=headers, data=payload)

    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())

  


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_create_project_with_invalid_token():
    url = EndpointPlanka.BASE_PROJECTS.value
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }
     
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.project_management
@pytest.mark.regression
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC003_validate_project_creation_response_payload(setup_add_project):
    get_token , created_projects = setup_add_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token 
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response , SCHEMA_OUTPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.payload_validation
@pytest.mark.regression
@pytest.mark.functional_positive
def test_TC004_validate_project_creation_request_payload(setup_add_project):
    get_token , created_projects = setup_add_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {
        'Authorization': f'Bearer {TOKEN_PLANKA}'
        }
    
    response = requests.post(url,headers=headers,json=PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_PROJECT_CREATE,SCHEMA_INPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC005_create_project_with_attribute_type_private(setup_add_project):
    get_token , created_projects = setup_add_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_PRIVATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC006_create_project_with_attribute_type_shared(setup_add_project):
    get_token , created_projects = setup_add_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_SHARED)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())
  


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC007_create_project_with_attribute_type_empty(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC008_create_project_with_attribute_type_invalid(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_TYPE_INVALID)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC009_create_project_with_attribute_name_empty(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_NAME_EMPTY)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG013: La atributo nombre del proyecto permite entradas numéricas ",run=True)
@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC010_create_project_with_attribute_name_value_number(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE_NAME_NUMBER)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_400(response)


