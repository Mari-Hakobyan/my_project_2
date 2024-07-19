import random
import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature('Resources Management')
@allure.story('Fetch Resources')
@pytest.mark.regression
@pytest.mark.parametrize('resource', ['unkown', 'kuku', 'mumu'])
def test_get_resource_list(resource):

    with allure.step("Send GET request to fetch resource"):
        response = requests.get(f"{BASE_URL}/{resource}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

@allure.feature('Resources Management')
@allure.story('Fetch single Resources')
@pytest.mark.regression
@pytest.mark.parametrize('id', [random.randint(1, 12) for _ in range(1, 5)])
def test_get_single_resource(id):

    with allure.step("Send GET request to fetch resourse"):
        response = requests.get(f"{BASE_URL}/unkown/{id}")
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200
    with allure.step("Verify the response data structure"):
        result = response.json()

        assert "data" in result
        assert result['data']['id']==id
        assert "name" in result['data']
        assert "year" in result['data']
        assert "color" in result['data']
        assert "pantone_value" in result['data']


@allure.feature('Resources Management')
@allure.story('Fetch Resources Not Found')
@pytest.mark.regression
@pytest.mark.parametrize('id', [random.randint(13, 50) for _ in range(1, 5)])
def test_get_not_found_resource(id):

    with allure.step("Send GET request to fetch resource"):
        response = requests.get(f"{BASE_URL}/unkown/{id}")
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404
    with allure.step("Verify the response data structure"):
        data = response.json()
        assert "data" not in data






