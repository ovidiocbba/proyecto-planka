import requests
import json
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200 
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST 



@pytest.mark.list
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_create_list(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_LIST)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.list
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_get_list_actual(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.list
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_delete_list_by_id(get_token , create_test_list):
    ID_LIST = create_test_list
    TOKEN_PLANKA = get_token
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_200(response)