import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('User Management')
@allure.story('Create User')
def test_create_user():
    user_data = {
        "name": "John Doe",
        "job": "Software Developer"
    }
    with allure.step("Send POST request to create a new user"):
        response = requests.post(f"{BASE_URL}/users", json=user_data)
    with allure.step("Verify the response status code is 201"):
        assert response.status_code == 201
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "id" in data
        assert data["name"] == user_data["name"]
        assert data["job"] == user_data["job"]
