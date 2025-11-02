import requests
from config import BASE_URI , TOKEN_INVALID ,ID_LIST_NOT_EXISTS,ID_LIST_EMPTY,ID_LIST_INVALID_STRING
from src.assertions.status_code import assert_status_code_200,assert_status_code_401,assert_status_code_404
import pytest


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC068_delete_list_with_valid_token(get_token , create_test_list):
    ID_LIST = create_test_list
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/lists/{ID_LIST}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC069_delete_list_with_invalid_token(create_test_list):
    ID_LIST = create_test_list
    url = f"{BASE_URI}/lists/{ID_LIST}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC070_delete_list_with_id_list_not_exists():
    url = f"{BASE_URI}/lists/{ID_LIST_NOT_EXISTS}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC071_delete_list_with_id_list_empty():
    url = f"{BASE_URI}/lists/{ID_LIST_EMPTY}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_404(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.equivalence_partition
def test_TC072_delete_list_with_id_list_invalid():
    url = f"{BASE_URI}/lists/{ID_LIST_INVALID_STRING}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_401(response)