import pytest
import requests

# POST


@pytest.fixture
def base_url():
    return " "


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
        "Authorization": " "
    }


def test_create_project_positive(base_url, my_payload, my_headers):
    payload = my_payload
    headers = my_headers
    response = requests.post(
        base_url + 'projects', json=payload, headers=headers)
    assert response.status_code == 201
    assert 'id' in response.json()


def test_create_project_negative_missing_field(base_url, my_headers):
    # Без обязательного поля

    payload = {}
    headers = my_headers
    response = requests.post(
        base_url + 'projects', json=payload, headers=headers)
    assert response.status_code == 400
    assert 'error' in response.json()


# PUT

def test_update_project_positive(base_url, my_payload, my_headers):
    payload = my_payload
    headers = my_headers
    creation_response = requests.post(
        base_url + 'projects', json=payload, headers=headers)
    project_id = creation_response.json()["id"]

    # Изменяем созданный проект
    update_payload = {"title": "Госбастер"}
    update_response = requests.put(
        base_url + f'projects/{
            project_id}', json=update_payload, headers=headers)
    assert update_response.status_code == 200

    # Получаем обновленную версию проекта с помощью GET-запроса
    fetch_response = requests.get(
        base_url + f'projects/{project_id}', headers=headers)
    assert fetch_response.status_code == 200

    fetched_data = fetch_response.json()
    # Проверяем, что значение ключа title изменилось на новое
    expected_title = update_payload['title']
    actual_title = fetched_data.get('title')
    assert actual_title == expected_title


def test_update_project_negative_no_id(base_url, my_headers):

    # Негативный тест попытки обновления несуществующего проекта.
    payload = {'title': 'New Name'}
    headers = my_headers
    no_id = 'no-id'
    response = requests.put(
        base_url + f'projects/{no_id}', json=payload, headers=headers)
    assert response.status_code == 404

# GET


def test_get_project_positive(base_url, my_payload, my_headers):
    payload = my_payload
    headers = my_headers
    creation_response = requests.post(
        base_url + 'projects', json=payload, headers=headers)
    project_id = creation_response.json()["id"]

    get_response = requests.get(
        base_url + f'projects/{project_id}', headers=headers)
    assert get_response.status_code == 200

    project_data = get_response.json()
    assert project_data['title'] == 'ГосУслуги2'


def test_get_project_negative_no_id(base_url, my_headers):
    headers = my_headers
    no_id = 'no-id'
    response = requests.get(base_url + f'projects/{no_id}', headers=headers)
    assert response.status_code == 404
