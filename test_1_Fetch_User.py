import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('User Management')
@allure.story('Fetch Users')
def test_get_users():
    with allure.step("Send GET request to fetch users"):
        response = requests.get(f"{BASE_URL}/users", params={"page": 1, "per_page": 2})
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

@allure.feature('User Management')
@allure.story('Fetch Single User')
def test_get_user():
    user_id = 2
    with allure.step("Send GET request to fetch a single user"):
        response = requests.get(f"{BASE_URL}/users/{user_id}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == user_id
