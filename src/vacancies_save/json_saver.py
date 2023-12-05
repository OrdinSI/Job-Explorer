import json
from src.vacancies_save.abstract_vacancy_save import VacancySaver


class JsonSaver(VacancySaver):
    """ Класс для сохранения информации о вакансиях в JSON-файл"""

    def add_vacancy(self, save_vacancy):
        """Сохраняет в файл vacancies"""
        indexed_vacancies = {str(index): vacancy for index, vacancy in enumerate(save_vacancy, 1)}
        with open('vacancies.json', "w", encoding='utf-8') as file:
            json.dump(indexed_vacancies, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        pass

    def get_vacancy(self):
        pass
