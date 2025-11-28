
import pytest
from utils.constans import TOKEN_INVALID , ID_CARD_NOT_EXISTS , ID_CARD_EMPTY,ID_CARD_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
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
          "TC023: delete_card_with_valid_token",
          "TC024: delete_card_with_invalid_token"
     ])

def test_delete_card_with_token(get_token,use_fixture,token_value,expected_status,id_card):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{id_card}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "id_card_actual,expected_status",
    [
       pytest.param(ID_CARD_NOT_EXISTS,404,
                   id="TC025: delete_card_with_nonexistent_id"),
        
        pytest.param(ID_CARD_EMPTY,400,
                   marks=pytest.mark.xfail(reason="BUG010: Código HTTP incorrecto se retorna 404 en lugar de 400 al consultar un recurso inexistente"),
                   id="TC026: delete_card_with_empty_id"),
        
        pytest.param(ID_CARD_INVALID_STRING,400,
                   id="TC027: delete_card_with_invalid_id_type")
    ])

def test_delete_card_with_id_card(get_token,id_card_actual,expected_status):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{id_card_actual}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status==404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)






