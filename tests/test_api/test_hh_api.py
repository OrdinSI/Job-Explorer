import requests_mock
from src.api.hh_api import HeadHunterApi

def test_get_vacancies():
    test_params = 'python'
    expected_response = {'items': []}

    with requests_mock.Mocker() as m:
        m.get('https://api.hh.ru/vacancies', json=expected_response, status_code=200)

        api = HeadHunterApi()

        response = api.get_vacancies(test_params)
        assert response == expected_response
