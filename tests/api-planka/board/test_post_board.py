
import pytest
from utils.constans import TOKEN_INVALID 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE,PAYLOAD_BOARD_EMPTY_NAME,PAYLOAD_BOARD_EMPTY_POSITION,PAYLOAD_BOARD_NAME_VALUE_NUMBER,PAYLOAD_BOARD_POSITION_NEGATIVE,PAYLOAD_BOARD_POSITION_INVALID_TYPE,PAYLOAD_BOARD_POSITION_LARGE
from src.resources.schemas.board_schema import SCHEMA_BOARD_OUTPUT
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
        "TC001: create_board_with_valid_token",
        "TC002: create_board_with_invalid_token"
    ])

def test_create_board_with_token(setup_board,use_fixture,token_value,expected_status,id_project):
    get_token, created_boards = (setup_board if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url, response, headers, PAYLOAD_BOARD_CREATE)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_boards.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
@pytest.mark.parametrize(
    "payload , expected_status",
    [
        pytest.param(PAYLOAD_BOARD_EMPTY_NAME,400,
                   id="TC003: create_board_with_attribute_name_empty"),

        pytest.param(PAYLOAD_BOARD_NAME_VALUE_NUMBER,400,
                  marks=pytest.mark.xfail(reason="BUG001: El atributo name permite entradas de valor numérico"),
                  id="TC004: create_card_board_with_attribute_name_invalid")
    ])

def test_post_board_validate_attribute_with_name(get_token,payload,expected_status,id_project):
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if  expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)
 


@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.payload_validation
@pytest.mark.parametrize(
    "payload , expected_status",
    [
       pytest.param(PAYLOAD_BOARD_EMPTY_POSITION,400,
                   id="TC005: create_board_with_attribute_position_empty"),

        pytest.param(PAYLOAD_BOARD_POSITION_NEGATIVE,400,
                  id="TC006: create_board_with_attribute_position_negative"),
        
        pytest.param(PAYLOAD_BOARD_POSITION_INVALID_TYPE,400,
                   id="TC007: create_board_with_attribute_position_invalid_type"),

        pytest.param(PAYLOAD_BOARD_POSITION_LARGE,400,
                  marks=pytest.mark.xfail(reason="BUG002: El campo position no tiene un valor limite de cantidad de digitos"),
                  id="TC008: create_board_with_attribute_position_large")

    ])

def test_post_board_validate_attribute_with_position(get_token,payload,expected_status,id_project):
       url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
       headers = {'Authorization': f'Bearer {get_token}'}
       response = PlankaRequests.post(url,headers,payload)
       log_request_response(url, response, headers, payload)
       if  expected_status==400:
           AssertionStatusCode.assert_status_code_400(response)
     

       

@pytest.mark.board
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.schema_validation
@pytest.mark.parametrize(
    "url_id_project , expected_status", [
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_NOT_EXISTS.value,404,
                     marks=pytest.mark.xfail(reason="BUG003:Código de respuesta incorrecto de (400) al solicitar crear tablero especificando el identificador (ID) de proyecto no existente"),

                   id="TC009: create_board_with_nonexistent_project_id"),
        
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_EMPTY.value,404,
                   id="TC010: create_board_with_empty_project_id"),
        
        pytest.param(EndpointPlanka.BASE_BOARDS_WITH_ID_PROJECT_INVALID.value,400,
                   id="TC011: create_board_with_invalid_project_id_type")
    ])

def test_post_board_with_project_id(get_token,url_id_project,expected_status):
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url_id_project,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url_id_project, response, headers, PAYLOAD_BOARD_CREATE)
    if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
    else:
        AssertionStatusCode.assert_status_code_400(response)




def test_TC012_validate_board_response_schema(setup_board,id_project):
    get_token,created_boards = setup_board
    TOKEN_PLANKA = get_token
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}/boards"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url, response, headers, PAYLOAD_BOARD_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_BOARD_OUTPUT)
    created_boards.append(response.json())

 
  