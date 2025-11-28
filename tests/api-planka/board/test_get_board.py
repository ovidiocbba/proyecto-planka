
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.schemas.board_schema import SCHEMA_BOARD_OUTPUT2
from src.assertions.assertion_general import assert_response_time
from src.assertions.schema_assertion import AssertionSchemas
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests




@pytest.mark.board
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
        "TC013: get_board_with_valid_token",
        "TC014: get_board_with_invalid_token"
    ])

def test_get_board_with_token(get_token,use_fixture,token_value,expected_status,id_board):
    TOKEN_PLANKA = (get_token if use_fixture else (token_value))

    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    print(f"Status code es Error?: {response.status_code}, Response: {response.text}")

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
    
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC015_validate_board_response_schema(get_token,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_BOARD_OUTPUT2)


   
@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC016_validate_board_response_time(get_token,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "url_id_board , expected_status", [
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_NOT_EXISTS.value,404,
                   id="TC017: get_board_with_nonexistent_board_id"),

        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_EMPTY.value,400,
                   marks=pytest.mark.xfail(reason=" BUG004: La aplicación retorna código 200 y muestra un mensaje en HTML al dejar vacio el identificador (ID) tablero"),
                   id="TC018: get_board_with_empty_board_id"),

        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_INVALID.value,400,
                   id="TC019: get_board_with_invalid_board_id_type")    
    ])

def test_get_board_with_board_id(get_token,url_id_board,expected_status):
     url = url_id_board
     headers = {'Authorization': f'Bearer {get_token}'}
     response = PlankaRequests.get(url,headers)
     log_request_response(url, response, headers)
     if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
     else:
        AssertionStatusCode.assert_status_code_400(response)
     
