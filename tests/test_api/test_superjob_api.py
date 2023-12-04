import requests_mock
from src.api.superjob_api import SuperJobApi


def test_get_vacancies():
    test_params = 'python'
    expected_response = {'objects': []}

    with requests_mock.Mocker() as m:
        m.get('https://api.superjob.ru/2.0/vacancies/', json=expected_response, status_code=200)

        api = SuperJobApi()

        response = api.get_vacancies(test_params)
        assert response == expected_response







