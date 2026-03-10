import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2/"


@pytest.fixture
def my_payload():
    return {
        "title": "ГосУслуги2",
        "users": {
            "5cfc4bde-600f-4c21-8260-80d87b72f5ec": "admin"
        }
    }


@pytest.fixture
def my_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
        
    }
