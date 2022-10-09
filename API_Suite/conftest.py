from API_Suite.ConnectHelper import ConnectHelper as api_connector
import pytest
import json

@pytest.fixture(scope="function")
def token(point):
    point.get_token()
    yield point

@pytest.fixture(scope="function")
def point():
    check = api_connector()
    yield check
