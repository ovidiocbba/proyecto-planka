import requests
import pytest
import jsonschema
from config import BASE_URI , TOKEN_INVALID , ID_CARD1
from src.assertions.status_code import assert_status_code_200,assert_status_code_401
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.project_schema import SCHEMA_CARD_WITHOUT_STOPWATCH,SCHEMA_CARD_WITH_STOPWATCH



@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC038_get_card_with_valid_token(get_token):
    url = f"{BASE_URI}/cards/{ID_CARD1}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC039_get_card_with_invalid_token():
    url = f"{BASE_URI}/cards/{ID_CARD1}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_401(response)

@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC040_validate_card_response_time(get_token):
    url = f"{BASE_URI}/cards/{ID_CARD1}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_response_time(response)


@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.schema_validation
def test_TC041_validate_card_response_schema(get_token):
    url = f"{BASE_URI}/cards/{ID_CARD1}"
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    stopwatch = data["item"].get("stopwatch")

    if stopwatch is None:
        jsonschema.validate(data, schema=SCHEMA_CARD_WITHOUT_STOPWATCH)
    else:
       jsonschema.validate(data, schema=SCHEMA_CARD_WITH_STOPWATCH)