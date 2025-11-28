
import pytest
from utils.constans import TOKEN_INVALID 
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD,PAYLOAD_CREATE_CARD_TYPE_EMPTY,PAYLOAD_CREATE_CARD_POSITION_EMPTY,PAYLOAD_CREATE_CARD_NAME_EMPTY,PAYLOAD_CREATE_CARD_TYPE_PROJECT,PAYLOAD_CREATE_CARD_TYPE_STORY , PAYLOAD_CREATE_CARD_TYPE_INVALID,PAYLOAD_CREATE_CARD_POSITION_INVALID,PAYLOAD_CREATE_CARD_NAME_INVALID,PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS
from src.resources.schemas.card_schema import SCHEMA_CARD_PAYLOAD_INPUT
from src.routes.endpoint import EndpointPlanka
from utils.logger_helper import log_request_response
from src.assertions.schema_assertion import AssertionSchemas
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
        "TC001: create_card_with_valid_token",
        "TC002: create_card_with_invalid_token"
    ])

def test_create_card_with_token(setup_card,use_fixture,token_value,expected_status,id_list):
    get_token, created_cards = (setup_card if use_fixture else (token_value, []))

    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)

    if expected_status == 200:
        AssertionStatusCode.assert_status_code_200(response)
        created_cards.append(response.json())
    else:
      AssertionStatusCode.assert_status_code_401(response)


    

@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
def test_TC003_validate_card_creation_request_payload(setup_card,id_list):
    get_token,created_cards = setup_card
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionSchemas.validate_input_schema(PAYLOAD_CREATE_CARD, SCHEMA_CARD_PAYLOAD_INPUT)
    created_cards.append(response.json())


   
@pytest.mark.card
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [(PAYLOAD_CREATE_CARD_TYPE_PROJECT,200),
     (PAYLOAD_CREATE_CARD_TYPE_STORY,200),
     (PAYLOAD_CREATE_CARD_TYPE_EMPTY,400),
     (PAYLOAD_CREATE_CARD_TYPE_INVALID,400)
    ],
    ids=[
        "TC004: create_card_with_type_project",
        "TC005: create_card_with_type_story",
        "TC006: create_card_with_type_empty",
        "TC007: create_card_with_type_invalid" 
    ])

def test_post_card_validate_attribute_with_type(setup_card,payload,expected_status,id_list):
    get_token,created_cards = setup_card
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==200:
        AssertionStatusCode.assert_status_code_200(response)
        created_cards.append(response.json())
    else:
        AssertionStatusCode.assert_status_code_400(response)
    


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status",
    [
        pytest.param(PAYLOAD_CREATE_CARD_POSITION_EMPTY,400,
                   id="TC008: create_card_with_attribute_position_empty"),

        pytest.param(PAYLOAD_CREATE_CARD_POSITION_INVALID,400,
                  id="TC009: create_card_with_attribute_position_invalid"),

        pytest.param(PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE,400,
                  id="TC010: create_card_with_attribute_position_value_negative"),

        pytest.param( PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS,400,
                 marks=pytest.mark.xfail(reason="BG006: El campo position permite ingresar numeros sin limite de digitos"),
                 id="TC011: create_card_with_attribute_position_value_exceeding")
    ])

def test_post_card_validate_attribute_with_position(get_token,payload,expected_status,id_list):
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)

    if expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)

    


@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.payload_validation
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "payload , expected_status", [
        pytest.param(PAYLOAD_CREATE_CARD_NAME_EMPTY,400,
                   id="TC012: create_card_with_attribute_name_empty"),

        pytest.param(PAYLOAD_CREATE_CARD_NAME_INVALID,400,
                  marks=pytest.mark.xfail(reason="BUG007: El campo name permite ingresar valores numericos"),
                  id="TC013: create_card_with_attribute_name_invalid")
    ])

def test_post_card_validate_attribute_with_name(get_token,payload,expected_status,id_list):
    url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}/cards"
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,payload)
    log_request_response(url, response, headers, payload)
    if expected_status==400:
        AssertionStatusCode.assert_status_code_400(response)
    
    
@pytest.mark.card
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
    "url_id_list , expected_status", [
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_NOT_EXISTS.value,404,
                   id="TC014: create_card_with_nonexistent_list_id"),
        
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_EMPTY.value,400,
                   marks=pytest.mark.xfail(reason="BUG008: Código HTTP incorrecto se retorna 404 en lugar de 400 al consultar un recurso vacio"),
                   id="TC015: create_card_with_empty_list_id"),
        
        pytest.param(EndpointPlanka.BASE_CARD_WITH_ID_LIST_INVALID.value,400,
                   id="TC016: create_card_with_invalid_list_id"),

    ])

def test_post_card_with_list_id(get_token,url_id_list,expected_status):
    url = url_id_list
    headers = {'Authorization': f'Bearer {get_token}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_CREATE_CARD)
    log_request_response(url, response, headers, PAYLOAD_CREATE_CARD)
    if expected_status==404:
        AssertionStatusCode.assert_status_code_404(response)
    else:
        AssertionStatusCode.assert_status_code_400(response)

    