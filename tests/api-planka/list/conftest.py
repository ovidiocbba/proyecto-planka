import pytest
from src.resources.payloads.list_payloads import PAYLOAD_CREATE_LIST
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from utils.logger_helper import get_logger



logger = get_logger("list_fixture")
@pytest.fixture(scope="function")
def setup_list(get_token):
    created_lists = []      
    logger.info("Setup iniciado para creación de listas")
    yield get_token,created_lists
     
    if created_lists:
        logger.info("Iniciando teardown: Eliminación de listas...")
        headers = {'Authorization': f'Bearer {get_token}'}
        for list in created_lists:
            list_id_to_delete = list.get("item", {}).get("id")
            url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{list_id_to_delete}"
            response = PlankaRequests.delete(url, headers)
            if response.status_code == 200:
                logger.info(f"Lista eliminada correctamente: {list_id_to_delete}")
            else:
                logger.info(
                    f"No se pudo eliminar la lista {list_id_to_delete}. "
                    f"Status: {response.status_code}"
                )
    else:
        logger.info("No hay listas creadas para eliminar.")
            


