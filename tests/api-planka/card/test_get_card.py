
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.assertions.assertion_general import assert_response_time
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests



@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.headers_validation
@pytest.mark.parametrize(
    "use_fixture,token_value,expected_status",
    [(True,None,200),
     (False,TOKEN_INVALID,401)
    ],
    ids=[
        "TC017: get_card_with_valid_token",
        "TC018: get_card_with_invalid_token"
    ])

def test_get_card_with_token(get_token,use_fixture,token_value,expected_status,id_card):
    TOKEN_PLANKA = (get_token if use_fixture else (token_value))

    url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{id_card}"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
    
    else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC019_validate_card_response_time(get_token,id_card):
    url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{id_card}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)



@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "url_id_card , expected_status", [
        pytest.param(EndpointPlanka.BASE_CARDS_WITH_ID_CARD_NOT_EXISTS.value,404,
                   id="TC020: get_card_with_nonexistent_card_id"),

        pytest.param(EndpointPlanka.BASE_CARDS_WITH_ID_CARD_VALUE_EMPTY.value,400, 
                   marks=pytest.mark.xfail(reason="BUG009: La aplicación retorna código 200 y muestra el mensaje: Necesitas habilitar JavaScript para ejecutar esta aplicación "),
                   id="TC021: get_card_with_empty_card_id"),
        
        pytest.param(EndpointPlanka.BASE_CARDS_WITH_ID_CARD_VALUE_INVALID.value,400,
                   id="TC022: get_card_with_invalid_card_id_type")  

    ])

def test_get_card_with_id_card(get_token,url_id_card,expected_status):
    url = url_id_card
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
    else:
        AssertionStatusCode.assert_status_code_400(response)



