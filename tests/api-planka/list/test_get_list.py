
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
@pytest.mark.functional_negative
@pytest.mark.headers_validation
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "TC018: get_list_with_valid_token",
          "TC019: get_list_with_invalid_token"
     ])

def test_get_list_with_token(get_token,use_fixture,token_value,expected_status,id_list):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.get(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)
   



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.performance
def test_TC020_validate_list_response_time(get_token,id_list):   
    TOKEN_PLANKA = get_token 
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    assert_response_time(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC021_validate_list_response_schema(get_token,id_list):   
    TOKEN_PLANKA = get_token 
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}"
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
@pytest.mark.parametrize(
   "url_id_list,expected_status",
    [
        pytest.param(EndpointPlanka.BASE_LIST_WITH_ID_LIST_NOT_EXISTS.value,404,
                   id="TC022: get_list_with_nonexistent_list_id"),

        pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_LIST_EMPTY.value,400, 
                   marks=pytest.mark.xfail(reason="BUG0013: La aplicación retorna código 200 y muestra el mensaje : Necesitas habilitar JavaScript para ejecutar esta aplicación"),
                   id="TC023: get_list_with_empty_list_id"),

        pytest.param(EndpointPlanka.BASE_LISTS_WITH_ID_LIST_INVALID.value,400,
                   id="TC024: get_list_with_invalid_list_id_type")  
    ])

def test_get_list_with_id_list_parametrizer(get_token,url_id_list,expected_status):
    url = url_id_list
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    if expected_status==404:
          AssertionStatusCode.assert_status_code_404(response)
    else:
      AssertionStatusCode.assert_status_code_400(response)
   












    


