import random
import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('User Management')
@allure.story('Fetch Users')
@allure.title('Test Retrieve All Users Information')
@allure.description('This test case verifies that the system retrieves all users')
@pytest.mark.regression
@pytest.mark.parametrize('page_number', [i for i in range(1, 3)])
def test_get_users(page_number):
    with allure.step("Send GET request to fetch users"):
        response = requests.get(f"{BASE_URL}/users?page={page_number}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

@allure.feature('User Management')
@allure.story('Fetch Users')
@allure.title('Test Retrieve All Users Information')
@allure.description('This test case verifies that the system retrieves all users')
@pytest.mark.regression
@pytest.mark.parametrize('page_number', [i for i in range(3, 15)])
def test_get_users_empty_list(page_number):
    with allure.step("Send GET request to fetch users"):
        response = requests.get(f"{BASE_URL}/users?page={page_number}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert len(data["data"]) == 0

@allure.feature('User Management')
@allure.story('Fetch Single User')
@allure.title('Test Retrieve Single User Information')
@allure.description('This test case verifies that the system retrieves single user')
@pytest.mark.smoke
@pytest.mark.parametrize('x', [random.randint(1, 12) for _ in range(1, 5)])
def test_get_user(x):
    id = x
    with allure.step("Send GET request to fetch a single user"):
        response = requests.get(f"{BASE_URL}/users/{id}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == id


@allure.feature('User Management')
@allure.story('Fetch Not Existing User')
@allure.title('Test NOT FOUND SINGLE USER')
@allure.description('This test case verifies that the system retrieves not existing user')
@pytest.mark.smoke
@pytest.mark.parametrize('x', [random.randint(13, 100) for _ in range(1, 5)])
def test_single_user_not_found(x):
    id = x
    with allure.step("Send GET request to fetch a single user"):
        response = requests.get(f"{BASE_URL}/users/{id}")
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404
    with allure.step("Verify the response is empty"):
        data = response.json()
        assert "data" not in data


