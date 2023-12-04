from typing import List, Dict, Any
import json

from src.vacancies_save.abstract_vacancy_save import VacancySaver


class JsonSaver(VacancySaver):
    """ Класс для сохранения информации о вакансиях в JSON-файл"""

    def add_vacancy(self, save_vacancy: List[Dict[str, Any]]):
        """Сохраняет в файл vacancies"""
        with open('file.json', "w", encoding='utf-8') as file:
            json.dump(save_vacancy, file, indent=4, ensure_ascii=False)


    def delete_vacancy(self):
        pass

    def get_vacancy(self):
        pass
