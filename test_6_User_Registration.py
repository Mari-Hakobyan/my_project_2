import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"
@allure.feature('Authentication')
@allure.story('User Registration')
def test_register():
    register_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    with allure.step("Send POST request to register a new user"):
        response = requests.post(f"{BASE_URL}/register", json=register_data)
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "token" in data

@allure.feature('Authentication')
@allure.story('Failed User Registration')
def test_register_fail():
    register_data = {
        "email": "sydney@fife"
    }
    with allure.step("Send POST request to register a user with missing password"):
        response = requests.post(f"{BASE_URL}/register", json=register_data)
    with allure.step("Verify the response status code is 400"):
        assert response.status_code == 400
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "error" in data
