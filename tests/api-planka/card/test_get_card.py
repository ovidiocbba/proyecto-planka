import requests
import pytest
import jsonschema
from config import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200,assert_status_code_401, assert_status_code_400,assert_status_code_404
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.card_schema import SCHEMA_CARD_WITHOUT_STOPWATCH,SCHEMA_CARD_WITH_STOPWATCH
from utils.logger_helper import log_request_response




@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC017_get_card_with_valid_token(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC018_get_card_with_invalid_token():
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD.value
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_401(response)



@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC019_validate_card_response_time(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_response_time(response)


@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC020_validate_card_response_schema(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_200(response)


    data = response.json()
    stopwatch = data["item"].get("stopwatch")

    if stopwatch is None:
        jsonschema.validate(data, schema=SCHEMA_CARD_WITHOUT_STOPWATCH)
    else:
       jsonschema.validate(data, schema=SCHEMA_CARD_WITH_STOPWATCH)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC021_get_card_with_nonexistent_card_id(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_404(response)



@pytest.mark.xfail(reason=" BUG008: La app muestra una pagina web con el texto : Necesitas habilitar JavaScript para ejecutar esta aplicación y con codigo 200 . Deberia retornar otro codigo ",run=True)
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC022_get_card_with_empty_card_id(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD_VALUE_EMPTY.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_400(response)


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC023_get_card_with_invalid_card_id_type(get_token):
    url = EndpointPlanka.BASE_CARDS_WITH_ID_CARD_VALUE_INVALID.value
    TOKEN_PLANKA = get_token
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    log_request_response(url, response, headers)
    assert_status_code_400(response)

