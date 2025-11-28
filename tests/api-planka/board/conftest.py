
import pytest
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE 
from utils.logger_helper import get_logger


logger = get_logger("board_fixture")


@pytest.fixture(scope="function")
def setup_board(get_token):
    created_boards = []
    logger.info("Setup iniciado para creación de tableros")
    yield get_token,created_boards

    if created_boards:
        logger.info("Iniciando teardown: Eliminación de tableros...")
        headers = {'Authorization': f'Bearer {get_token}'}
        for board in created_boards:
            board_id = board.get("item", {}).get("id")
            delete_url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{board_id}"
            response = PlankaRequests.delete(delete_url, headers)
            if response.status_code == 200:
                logger.info(f"Tablero eliminado correctamente: {board_id}")
            else:
                logger.info(
                    f"No se pudo eliminar el tablero {board_id}. "
                    f"Status: {response.status_code}"
                )
    else:
        logger.info("No hay tableros creados para eliminar.")








   