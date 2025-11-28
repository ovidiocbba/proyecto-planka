
import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST,PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_ACTIVE,PAYLOAD_CREATE_LIST_TYPE_CLOSED,PAYLOAD_CREATE_LIST_EMPTY_TYPE,PAYLOAD_CREATE_LIST_EMPTY_POSITION,PAYLOAD_CREATE_LIST_EMPTY_NAME,PAYLOAD_CREATE_LIST_INVALID_TYPE,PAYLOAD_CREATE_LIST_INVALID_POSITION ,PAYLOAD_CREATE_LIST_INVALID_NAME,PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS
from src.resources.schemas.list_schema import SCHEMA_CREATE_LIST_OUTPUT,SCHEMA_LIST_PAYLOAD_INPUT
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
from src.routes.request import PlankaRequests


@pytest.mark.list
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
        "TC001: create_list_with_valid_token",
        "TC002: create_list_with_invalid_token"
    ])

def test_create_list_with_token(setup_list,use_fixture,token_value,expected_status,id_board):
    get_token, created_lists = (setup_list if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_lists.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        (PAYLOAD_CREATE_LIST_TYPE_ACTIVE, 200),
        (PAYLOAD_CREATE_LIST_TYPE_CLOSED, 200),
        (PAYLOAD_CREATE_LIST_EMPTY_TYPE, 400),
        (PAYLOAD_CREATE_LIST_INVALID_TYPE, 400)
    ],

    ids=[
        "TC003 : create_list_with_type_active",
        "TC004 : create_list_with_type_closed",
        "TC005 : create_list_with_type_empty",
        "TC006 : create_list_with_type_invalid",
    ])

def test_create_list_with_attribute_type_parametrizer(setup_list,payload,expected_status,id_board):
    get_token, created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}

    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_lists.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_400(response)
    



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload,expected_status",
    [
        pytest.param(PAYLOAD_CREATE_LIST_EMPTY_POSITION,400,
                   id="TC007: create_list_with_attribute_position_empty"),

        pytest.param(PAYLOAD_CREATE_LIST_INVALID_POSITION,400,
                  id="TC008: create_list_with_attribute_position_invalid"),


        pytest.param(PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE,400,
                  id="TC009: create_list_with_attribute_position_value_negative"),

        pytest.param(PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS,400,
                 marks=pytest.mark.xfail(reason="BUG011: El campo position permite ingresar numeros sin limite de digitos "),
                  id="TC010: create_list_with_attribute_position_value_exceeding")

 ])

def test_create_list_with_attribute_position_parametrizer(get_token,payload,expected_status,id_board):
   url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,payload)
   log_request_response(url, response, headers, payload)
   
   if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
        "payload,expected_status",
        [
            pytest.param(PAYLOAD_CREATE_LIST_EMPTY_NAME,400,
                    id="TC011: create_list_with_attribute_name_empty"),

            pytest.param(PAYLOAD_CREATE_LIST_INVALID_NAME,400,
                    marks=pytest.mark.xfail(reason="BUG012: El campo name permite ingresar valores numericos",run=True),
                    id="TC012: create_list_with_attribute_name_invalid")
        ])

def test_create_list_with_attribute_name_parametrizer(get_token,payload,expected_status,id_board):
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==400:
      AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC013_validate_list_creation_response_schema(setup_list,id_board):
    get_token,created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_output_schema(response,SCHEMA_CREATE_LIST_OUTPUT)
    created_lists.append(response.json())

   

@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC014_validate_list_creation_request_payload(setup_list,id_board):
    get_token,created_lists = setup_list
    url = f"{EndpointPlanka.BASE_LISTS.value}/{id_board}/lists"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_LIST,SCHEMA_LIST_PAYLOAD_INPUT)
    created_lists.append(response.json())

    

@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "url_id_board,expected_status",[
      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_NOT_EXISTS.value,404,
                   id="TC015: create_list_with_id_board_not_exists"),

      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_EMPTY.value,404,
                   id="TC016: create_list_with_id_board_empty"),
      
      pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_INVALID.value,400,
                   id="TC017: create_list_with_id_board_invalid_type")

   ])

def test_create_list_with_id_board_parametrizer(get_token,url_id_board,expected_status):
   url = url_id_board
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
   log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
   if expected_status==404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)

   
  