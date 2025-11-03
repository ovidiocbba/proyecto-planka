import requests
import json
import pytest
from src.assertions.status_code import assert_status_code_200 
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD 
from src.routes.endpoint import EndpointPlanka


@pytest.mark.card
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_create_card(get_token):
    url = EndpointPlanka.BASE_CARDS.value
    TOKEN_PLANKA = get_token
    payload = json.dumps(PAYLOAD_CREATE_CARD)
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_get_card_actual(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.e2e
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_delete_card_by_id(get_token,post_card):
  ID_CARD = post_card
  TOKEN_PLANKA = get_token
  url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{ID_CARD}"
  headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
  }

  response = requests.delete(url, headers=headers)
  assert_status_code_200(response)