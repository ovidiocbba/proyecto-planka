
import pytest
from utils.constans import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.list_schema import SCHEMA_ITEM_LIST , SCHEMA_INCLUDED_LIST
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
from src.routes.request import PlankaRequests




@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC018_get_list_with_valid_token(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC019_get_list_with_invalid_token():    
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {'Authorization': f'Bearer {TOKEN_INVALID}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC020_validate_list_response_time(get_token):   
    TOKEN_PLANKA = get_token 
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC021_validate_list_response_schema(get_token):   
    TOKEN_PLANKA = get_token 
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    data = response.json()
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_list_output_schema(data["item"],SCHEMA_ITEM_LIST)
    AssertionSchemas.validate_list_output_schema(data["included"],SCHEMA_INCLUDED_LIST)
    



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC022_get_list_with_nonexistent_list_id(get_token):  
    url = EndpointPlanka.BASE_LIST_WITH_ID_LIST_NOT_EXISTS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_404(response)



@pytest.mark.xfail(reason=" BUG0012: La aplicación retorna código 200 y muestra el mensaje : Necesitas habilitar JavaScript para ejecutar esta aplicación ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC023_get_list_with_empty_list_id(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST_EMPTY.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_404(response)
    



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC024_get_list_with_invalid_list_id_type(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST_INVALID.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_400(response)
    



