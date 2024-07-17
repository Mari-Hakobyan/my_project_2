import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('Authentication')
@allure.story('User Logout')
def test_logout():
    with allure.step("Send POST request to log out"):
        response = requests.post(f"{BASE_URL}/logout")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
