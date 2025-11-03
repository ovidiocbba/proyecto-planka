import pytest
import requests
from config import BASE_URI
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE
from src.routes.endpoint import EndpointPlanka


@pytest.fixture(scope="module")
def create_test_project(get_token):
      url = EndpointPlanka.BASE_PROJECTS.value
      TOKEN_PLANKA = get_token
      headers = {
        'Authorization': f'Bearer {TOKEN_PLANKA}'
      }

      response = requests.post(url,headers=headers,json=PAYLOAD_PROJECT_CREATE)
      data = response.json()
      project_id = data["item"]["id"]
      yield project_id
   
      delete_url = f"{BASE_URI}/projects/{project_id}"
      delete_response = requests.delete(delete_url,headers=headers)
      if delete_response.status_code != 200:
             print(f"Teardown: no se pudo borrar el proyecto {project_id}: {delete_response.text}")

  

    