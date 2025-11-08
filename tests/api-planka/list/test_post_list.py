
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
@pytest.mark.headers_validation
def test_TC001_create_list_with_valid_token(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers,PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_200(response)
    created_lists.append(response.json())


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC002_create_list_with_invalid_token():
    url = EndpointPlanka.BASE_LISTS.value
    headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC003_post_list_with_attribute_type_active(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_TYPE_ACTIVE)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_TYPE_ACTIVE)
    AssertionStatusCode.assert_status_code_200(response)
    created_lists.append(response.json())



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC004_post_list_with_attribute_type_closed(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_TYPE_CLOSED)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_TYPE_CLOSED)
    AssertionStatusCode.assert_status_code_200(response)
    created_lists.append(response.json())




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC005_post_list_attribute_with_type_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_EMPTY_TYPE)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_EMPTY_TYPE)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC006_post_list_attribute_with_type_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_INVALID_TYPE)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_INVALID_TYPE)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC007_post_list_attribute_with_position_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_EMPTY_POSITION)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_EMPTY_POSITION)
    AssertionStatusCode.assert_status_code_400(response)
 


@pytest.mark.xfail(reason=" BUG009: La atributo position  permite entradas de cadena ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC008_post_list_attribute_with_position_invalid(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_INVALID_POSITION)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_INVALID_POSITION)
    AssertionStatusCode.assert_status_code_400(response)
    created_lists.append(response.json())



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC009_post_list_attribute_position_with_value_negative(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE)
    AssertionStatusCode.assert_status_code_400(response)



@pytest.mark.xfail(reason=" BUG010: El campo position permite ingresar numeros sin limite de digitos ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC010_post_list_with_position_value_exceeding(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS)
    AssertionStatusCode.assert_status_code_400(response)
    created_lists.append(response.json())






@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC011_post_list_attribute_with_name_empty(get_token):
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_EMPTY_NAME)
    log_request_response(url, response, headers,PAYLOAD_CREATE_LIST_EMPTY_NAME)
    AssertionStatusCode.assert_status_code_400(response)




@pytest.mark.xfail(reason=" BUG011: El campo name permite ingresar valores numericos ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
def test_TC012_post_list_attribute_with_name_invalid(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST_INVALID_NAME)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST_INVALID_NAME)
    AssertionStatusCode.assert_status_code_400(response)
    created_lists.append(response.json())



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC013_validate_list_creation_response_schema(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
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
def test_TC014_validate_list_creation_request_payload(setup_add_list):
    get_token,created_lists = setup_add_list
    url = EndpointPlanka.BASE_LISTS.value
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
def test_TC015_post_list_with_id_board_not_exists(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_400_or_404(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC016_post_list_with_id_board_empty(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_EMPTY.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_404(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC017_post_list_with_id_board_invalid(get_token):
    url = EndpointPlanka.BASE_LISTS_WITH_ID_BOARD_INVALID.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_LIST)
    log_request_response(url, response, headers, PAYLOAD_CREATE_LIST)
    AssertionStatusCode.assert_status_code_400(response)
    