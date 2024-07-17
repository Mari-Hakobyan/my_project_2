import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('User Management')
@allure.story('Delete User')
def test_delete_user():
    user_id = 2
    with allure.step("Send DELETE request to remove a user"):
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
    with allure.step("Verify the response status code is 204"):
        assert response.status_code == 204