import requests
from config import BASE_URI , TOKEN_INVALID , ID_CARD_NOT_EXISTS , ID_CARD_EMPTY,ID_CARD_INVALID_STRING
from src.assertions.status_code import assert_status_code_200 ,assert_status_code_400 , assert_status_code_401,assert_status_code_404
import pytest


@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC042_delete_card_with_valid_token(get_token,post_card):
  ID_CARD = post_card
  TOKEN_PLANKA = get_token
  url = f"{BASE_URI}/cards/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC043_delete_card_with_invalid_token(post_card): 
  ID_CARD = post_card
  url = f"{BASE_URI}/cards/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_401(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC044_delete_card_with_nonexistent_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{BASE_URI}/cards/{ID_CARD_NOT_EXISTS}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC045_delete_card_with_empty_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{BASE_URI}/cards/{ID_CARD_EMPTY}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_404(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC046_delete_card_with_invalid_id(get_token): 
  TOKEN_PLANKA = get_token
  url = f"{BASE_URI}/cards/{ID_CARD_INVALID_STRING}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_400(response)