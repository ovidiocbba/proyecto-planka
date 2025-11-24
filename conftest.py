import pytest
from utils.auth_token import generate_token

@pytest.fixture(scope="session")
def get_token():
    access_token = generate_token()
    return access_token











    