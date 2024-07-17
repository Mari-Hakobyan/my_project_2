import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('Authentication')
@allure.story('User Login')
def test_login():
    login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    with allure.step("Send POST request to log in"):
        response = requests.post(f"{BASE_URL}/login", json=login_data)
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "token" in data

@allure.feature('Authentication')
@allure.story('Failed User Login')
def test_login_fail():
    login_data = {
        "email": "eve.holt@reqres.in"
    }
    with allure.step("Send POST request to log in with missing password"):
        response = requests.post(f"{BASE_URL}/login", json=login_data)
    with allure.step("Verify the response status code is 400"):
        assert response.status_code == 400
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "error" in data
