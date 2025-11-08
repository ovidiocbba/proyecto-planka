
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
@pytest.mark.headers_validation
def test_TC013_get_board_with_valid_token(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC014_get_board_with_invalid_token():
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC015_validate_board_response_schema(get_token):
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_BOARD_OUTPUT2)


   
@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC016_validate_board_response_time(get_token):
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC017_get_board_with_nonexistent_board_id(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_NOT_EXISTS.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_404(response)



@pytest.mark.xfail(reason=" BUG004: La aplicación retorna código 200 y muestra el mensaje : Necesitas habilitar JavaScript para ejecutar esta aplicación ",run=True)
@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC018_get_board_with_empty_board_id(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_EMPTY.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC019_get_board_with_invalid_board_id_type(get_token):
    TOKEN_PLANKA = get_token
    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD_INVALID.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_400(response)