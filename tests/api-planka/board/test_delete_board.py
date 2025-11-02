import requests
import pytest
from config import BASE_URI , TOKEN_INVALID , ID_BOARD2 , ID_BOARD_NOT_EXISTS , ID_BOARD_EMPTY ,ID_BOARD_INVALID_STRING
from src.assertions.status_code import assert_status_code_200, assert_status_code_400,assert_status_code_401 , assert_status_code_404


@pytest.mark.board
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC017_delete_board_with_valid_token(get_token,post_test_board):
    TOKEN_PLANKA = get_token
    ID_BOARD =  post_test_board
    url = f"{BASE_URI}/boards/{ID_BOARD}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_200(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC018_delete_board_with_invalid_token():
    url = f"{BASE_URI}/boards/{ID_BOARD2}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_401(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC019_delete_board_with_nonexistent_id(get_token):
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/boards/{ID_BOARD_NOT_EXISTS}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_404(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC020_delete_board_with_empty_id(get_token):
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/boards/{ID_BOARD_EMPTY}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_404(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC021_delete_board_with_invalid_id_type(get_token):
    TOKEN_PLANKA = get_token
    url = f"{BASE_URI}/boards/{ID_BOARD_INVALID_STRING}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA} '
    }
    response = requests.delete(url, headers=headers)
    assert_status_code_400(response)