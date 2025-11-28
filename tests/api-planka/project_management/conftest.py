import pytest
from src.routes.endpoint import EndpointPlanka
from src.routes.request import PlankaRequests
from utils.logger_helper import get_logger

logger = get_logger("project_fixture")



@pytest.fixture(scope="function")
def setup_project(get_token):
     created_projects = []
     logger.info("Setup iniciado para creación de proyectos")
     yield get_token , created_projects
     
      # ---------- TEARDOWN ----------
     if created_projects:
        logger.info("Iniciando teardown: Eliminación de proyectos...")
        headers = {'Authorization': f'Bearer {get_token}'}

        for project in created_projects:
            project_id = project.get("item", {}).get("id") 
            url = f"{EndpointPlanka.BASE_PROJECTS.value}/{project_id}"
            response = PlankaRequests.delete(url, headers)
            if response.status_code == 200:
                logger.info(f"Proyecto eliminado correctamente: {project_id}")
            else:
                logger.info(
                    f"No se pudo eliminar el proyecto {project_id}. "
                    f"Status: {response.status_code}"
                )
     else:
        logger.info("No hay proyectos creados para eliminar.")
          



     