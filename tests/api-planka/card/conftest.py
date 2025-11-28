
import pytest
from src.resources.payloads.card_payloads import PAYLOAD_CREATE_CARD
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from utils.logger_helper import get_logger


logger = get_logger("card_fixture")

@pytest.fixture(scope="module")
def setup_card(get_token):
    created_card = []
    logger.info("Setup iniciado para creación de cards")
    yield get_token, created_card

    if created_card:
        logger.info("Iniciando teardown: Eliminación de cards...")
        headers = {'Authorization': f'Bearer {get_token}'}
        for card in created_card:
            card_id_to_delete = card.get("item", {}).get("id")
            url = f"{EndpointPlanka.BASE_CARD_MAJOR.value}/{card_id_to_delete}"
            #http://localhost:3000/api/cards/{{ID_CARD1}}
            response = PlankaRequests.delete(url, headers)  
            if response.status_code == 200:
                logger.info(f"Card eliminada correctamente: {card_id_to_delete}")
            else:
                logger.info(
                    f"No se pudo eliminar la card {card_id_to_delete}. "
                    f"Status: {response.status_code}"
                )
    else:
        logger.info("No hay cards creadas para eliminar.")  