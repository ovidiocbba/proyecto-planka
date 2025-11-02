import requests
import pytest
import jsonschema
from config import BASE_URI , ID_LIST1 , TOKEN_INVALID
from src.assertions.status_code import assert_status_code_200,assert_status_code_401
from src.assertions.assertion_general import assert_response_time
from src.resources.schemas.project_schema import SCHEMA_ITEM_LIST , SCHEMA_INCLUDED_LIST


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_TC064_get_list_with_valid_token(get_token):    
    url = f"{BASE_URI}/lists/{ID_LIST1}"
    TOKEN_PLANKA = get_token

    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_200(response)



@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.headers_validation
def test_TC065_get_list_with_invalid_token():    
    url = f"{BASE_URI}/lists/{ID_LIST1}"
    headers = {
    'Authorization': f'Bearer {TOKEN_INVALID}'
    }

    response = requests.get(url, headers=headers)
    assert_status_code_401(response)


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.response_time 
def test_TC066_validate_list_response_time(get_token):   
    TOKEN_PLANKA = get_token 
    url = f"{BASE_URI}/lists/{ID_LIST1}"
    headers = {
    'Authorization': f'Bearer {TOKEN_PLANKA}'
    }

    response = requests.get(url, headers=headers)
    assert_response_time(response)



@pytest.mark.list
@pytest.mark.functional_positive
@pytest.mark.schema_validation
def test_TC067_validate_list_response_schema(get_token):   
    TOKEN_PLANKA = get_token 
    url = f"{BASE_URI}/lists/{ID_LIST1}"
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