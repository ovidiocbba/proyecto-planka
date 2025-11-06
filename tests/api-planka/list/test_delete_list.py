import requests
import pytest
from config import TOKEN_INVALID ,ID_LIST_NOT_EXISTS,ID_LIST_EMPTY,ID_LIST_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200,assert_status_code_401,assert_status_code_404
from utils.logger_helper import log_request_response



@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC025_delete_list_with_valid_token(get_token , create_test_list):
    ID_LIST = create_test_list
    TOKEN_PLANKA = get_token
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC026_delete_list_with_invalid_token(create_test_list):
    ID_LIST = create_test_list
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC027_delete_list_with_id_list_not_exists():
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST_NOT_EXISTS}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC028_delete_list_with_id_list_empty():
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST_EMPTY}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_404(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC029_delete_list_with_id_list_invalid():
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST_INVALID_STRING}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_401(response)