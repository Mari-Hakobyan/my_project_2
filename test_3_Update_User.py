import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('User Management')
@allure.story('Update User')
def test_update_user():
    user_id = 2
    user_data = {
        "name": "Jane Doe",
        "job": "Manager"
    }
    with allure.step("Send PUT request to update an existing user"):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=user_data)
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert data["name"] == user_data["name"]
        assert data["job"] == user_data["job"]

@allure.feature('User Management')
@allure.story('Partially Update User')
def test_patch_user():
    user_id = 2
    user_data = {
        "name": "Jane Doe"
    }
    with allure.step("Send PATCH request to partially update an existing user"):
        response = requests.patch(f"{BASE_URL}/users/{user_id}", json=user_data)
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert data["name"] == user_data["name"]
