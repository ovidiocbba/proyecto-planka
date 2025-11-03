import requests
import pytest
import jsonschema
from config import TOKEN_INVALID
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code import assert_status_code_200, assert_status_code_400,assert_status_code_401 , assert_status_code_404
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.list_schema import SCHEMA_ITEM_LIST , SCHEMA_INCLUDED_LIST


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC018_get_list_with_valid_token(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC019_get_list_with_invalid_token():    
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.performance

def test_TC020_validate_list_response_time(get_token):   
    TOKEN_PLANKA = get_token 
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_response_time(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.regression
@pytest.mark.schema_validation
def test_TC021_validate_list_response_schema(get_token):   
    TOKEN_PLANKA = get_token 
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST.value
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
   
    assert_status_code_200(response)


    try:
        jsonschema.validate(instance=data["item"], schema=SCHEMA_ITEM_LIST)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"JSON schema for 'item' doesn't match: {e}")


    try:
        jsonschema.validate(instance=data["included"], schema=SCHEMA_INCLUDED_LIST)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"JSON schema for 'included' doesn't match: {e}")


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC022_get_list_with_nonexistent_list_id(get_token):  
    url = EndpointPlanka.BASE_LIST_WITH_ID_LIST_NOT_EXISTS.value
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_404(response)


@pytest.mark.xfail(reason=" BUG0012: La app muestra una pagina web con el texto : Necesitas habilitar JavaScript para ejecutar esta aplicación y con codigo 200 . Deberia retornar otro codigo ",run=True)
@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC023_get_list_with_empty_list_id(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST_EMPTY.value
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_404(response)


@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
def test_TC024_get_list_with_invalid_list_id_type(get_token):  
    url = EndpointPlanka.BASE_LISTS_WITH_ID_LIST_INVALID.value
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_400(response)



