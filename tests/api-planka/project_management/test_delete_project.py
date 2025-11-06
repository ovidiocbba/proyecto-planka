import requests
import pytest
from config import TOKEN_INVALID , ID_PROJECT_INVALID_STRING,ID_PROJECT_NOT_EXISTS,ID_PROJECT_EMPTY 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200 , assert_status_code_400,assert_status_code_404, assert_status_code_401,assert_status_code_400_or_404
from utils.logger_helper import log_request_response



@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.smoke
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
def test_TC015_delete_project_with_valid_token(get_token, create_test_project):
    ID_PROJECT = create_test_project
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)

    
@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC016_delete_project_with_invalid_token(create_test_project):
   ID_PROJECT = create_test_project
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT}"
   headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

   response = requests.delete(url,headers=headers)
   log_request_response(url, response, headers)
   assert_status_code_401(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC017_delete_project_for_id_not_exists(get_token):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT_NOT_EXISTS}"
   headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

   response = requests.delete(url,headers=headers)
   log_request_response(url, response, headers)
   assert_status_code_400_or_404(response)


@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC018_delete_project_for_id_invalid_empty(get_token):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT_EMPTY}"
   headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

   response = requests.delete(url,headers=headers)
   log_request_response(url, response, headers)
   assert_status_code_404(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC019_delete_project_for_id_invalid_string(get_token):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT_INVALID_STRING}"
   headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

   response = requests.delete(url,headers=headers)
   log_request_response(url, response, headers)
   assert_status_code_400(response)

   