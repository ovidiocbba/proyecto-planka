import requests
import json
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE 

from utils.logger_helper import log_request_response




@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_create_project(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_PROJECT_CREATE)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }
    response = requests.post(url, headers=headers, data=payload)
    log_request_response(url, response, headers, payload)
    AssertionStatusCode.assert_status_code_200(response)




@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_get_projects(get_token):
    url = EndpointPlanka.BASE_PROJECTS.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)





@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.smoke
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
def test_delete_project_by_id(get_token, create_test_project):
    ID_PROJECT = create_test_project
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)



