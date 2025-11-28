
import pytest
from utils.constans import TOKEN_INVALID, ID_BOARD_NOT_EXISTS , ID_BOARD_EMPTY ,ID_BOARD_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
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
          "TC020: delete_board_with_valid_token",
          "TC021: delete_board_with_invalid_token"
     ])

def test_delete_board_with_token(get_token,use_fixture,token_value,expected_status,id_board):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{id_board}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.board
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_board , expected_status",[
        pytest.param(ID_BOARD_NOT_EXISTS,404,
                   id="TC022: delete_board_with_nonexistent_id"),
        
        pytest.param(ID_BOARD_EMPTY,400,
                   marks=pytest.mark.xfail(reason="BUG005: Código de respuesta incorrecto de (404) al solicitar eliminar un tablero sin especificar su identificador (ID)"),
                   id="TC023: delete_board_with_empty_id"),
        
        pytest.param(ID_BOARD_INVALID_STRING,400,
                   id="TC024: delete_board_with_invalid_id_type")

    ])

def test_delete_board_with_board_id(get_token,id_board,expected_status):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{id_board}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA} '}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status==404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)






