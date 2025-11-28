
import pytest
from utils.constans import TOKEN_INVALID , ID_PROJECT_INVALID_STRING,ID_PROJECT_NOT_EXISTS,ID_PROJECT_EMPTY 
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests




@pytest.mark.project_management
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.smoke
@pytest.mark.headers_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "TC015: delete_project_with_valid_token",
          "TC016: delete_project_with_invalid_token"
     ])

def test_delete_project_with_token(get_token,use_fixture,token_value,expected_status,id_project):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)



@pytest.mark.project_management
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition

@pytest.mark.parametrize(
   "id_project,expected_status",[
         pytest.param(ID_PROJECT_NOT_EXISTS,400,
                  id="TC017: delete_project_with_id_not_exists"),

         pytest.param(ID_PROJECT_EMPTY,404,
                  id="TC018: delete_project_with_id_empty"),

         pytest.param(ID_PROJECT_INVALID_STRING,400,
                  id="TC019: delete_project_with_id_invalid_string")
  ])

def test_delete_project_with_id_parametrizer(get_token,id_project,expected_status):
   url = f"{EndpointPlanka.BASE_PROJECTS.value}/{id_project}"
   headers = {'Authorization': f'Bearer {get_token}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status == 404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)




