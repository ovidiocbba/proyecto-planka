import requests
import pytest
import jsonschema
from config import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200 , assert_status_code_401
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.project_schema import SCHEMA_OUTPUT_GET_PROJECTS


@pytest.mark.project_management
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC011_get_project_with_valid_token(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC012_get_project_with_invalid_token():
    url = EndpointPlanka.BASE_PROJECTS.value
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url,headers=headers)
    assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC013_get_project_validate_schema_output(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {
          'Authorization': f'Bearer {TOKEN_PLANKA}'
    }    
    response = requests.get(url,headers=headers)
    assert_status_code_200(response)
    

    try:
            jsonschema.validate(instance=response.json(), schema= SCHEMA_OUTPUT_GET_PROJECTS)
    except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC014_get_project_validate_response_time(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {
            'Authorization': f'Bearer {TOKEN_PLANKA}'
      }    
      
      response = requests.get(url,headers=headers)
      assert_response_time(response)
      