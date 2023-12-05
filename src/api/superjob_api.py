import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.api.abstract_api import Api


class SuperJobApi(Api):
    """Класс для работы с API SuperJob"""

    def __init__(self) -> None:
        load_dotenv()
        self.secret_key = os.getenv('Secret_Key')

    def get_vacancies(self, request: str) -> Dict[str, Any]:
        """Получение вакансий с SuperJob по запросу"""
        params = dict(keyword=request)
        headers = {"X-Api-App-Id": self.secret_key}
        res = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        return res.json()
