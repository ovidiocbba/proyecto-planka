import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE , PAYLOAD_PROJECT_CREATE_NAME_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_EMPTY ,PAYLOAD_PROJECT_CREATE_TYPE_SHARED,PAYLOAD_PROJECT_CREATE_TYPE_INVALID,PAYLOAD_PROJECT_CREATE_NAME_NUMBER
from src.resources.schemas.project_schema import SCHEMA_INPUT_CREATE_PROJECT,SCHEMA_OUTPUT_CREATE_PROJECT
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.headers_validation
@pytest.mark.parametrize(
    "use_fixture,token_value,expected_status",
    [(True,None,200),
     (False,TOKEN_INVALID,401)
    ],
    ids=[
        "TC001: create_project_with_valid_token",
        "TC002: create_project_with_invalid_token"
    ])

def test_create_project_with_token(setup_project,use_fixture,token_value,expected_status):
    get_token, created_projects = (setup_project if use_fixture else (token_value, []))

    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_projects.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.regression
@pytest.mark.functional_positive
@pytest.mark.payload_validation
def test_TC003_validate_project_creation_response_payload(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token 
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response , SCHEMA_OUTPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.payload_validation
@pytest.mark.regression
@pytest.mark.functional_positive
def test_TC004_validate_project_creation_request_payload(setup_project):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_PROJECT_CREATE,SCHEMA_INPUT_CREATE_PROJECT)
    created_projects.append(response.json())



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        (PAYLOAD_PROJECT_CREATE, 200),
        (PAYLOAD_PROJECT_CREATE_TYPE_SHARED, 200),
        (PAYLOAD_PROJECT_CREATE_TYPE_EMPTY, 400),
        (PAYLOAD_PROJECT_CREATE_TYPE_INVALID, 400)
    ],

    ids=[
        "TC005 : create_project_with_type_private",
        "TC006 : create_project_with_type_shared",
        "TC007 : create_project_with_type_empty",
        "TC008 : create_project_with_type_invalid",
    ])

def test_create_project_with_attribute_type_parametrizer(setup_project,payload,expected_status):
    get_token , created_projects = setup_project
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {'Authorization': f'Bearer {get_token}'}

    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_projects.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_400(response)
    


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload,expected_status",
    [
      pytest.param(PAYLOAD_PROJECT_CREATE_NAME_EMPTY,400,
                   id="TC009: create_project_with_attribute_name_empty"),

      pytest.param(PAYLOAD_PROJECT_CREATE_NAME_NUMBER,400,
                  marks=pytest.mark.xfail(reason="BUG014: El campo name del proyecto permite entradas numéricas",run=True),
                  id="TC010: create_project_with_attribute_name_value_number"
        )
    ])

def test_create_project_with_attribute_name_parametrizer(get_token,payload,expected_status):
   url = EndpointPlanka.BASE_PROJECTS.value
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,payload)
   log_request_response(url, response, headers, payload)
   if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)
   
   
   

