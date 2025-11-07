import requests
import pytest
from config import TOKEN_INVALID , ID_CARD_NOT_EXISTS , ID_CARD_EMPTY,ID_CARD_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response


@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC024_delete_card_with_valid_token(get_token,post_card):
  ID_CARD = post_card
  TOKEN_PLANKA = get_token
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  log_request_response(url, response, headers)
  AssertionStatusCode.assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC025_delete_card_with_invalid_token(post_card): 
  ID_CARD = post_card
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
  }

  response = requests.delete(url, headers=headers)
  log_request_response(url, response, headers)
  AssertionStatusCode.assert_status_code_401(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
def test_TC026_delete_card_with_nonexistent_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD_NOT_EXISTS}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  log_request_response(url, response, headers)
  AssertionStatusCode.assert_status_code_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC027_delete_card_with_empty_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD_EMPTY}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  log_request_response(url, response, headers)
  AssertionStatusCode.assert_status_code_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC028_delete_card_with_invalid_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD_INVALID_STRING}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  log_request_response(url, response, headers)
  AssertionStatusCode.assert_status_code_400(response)