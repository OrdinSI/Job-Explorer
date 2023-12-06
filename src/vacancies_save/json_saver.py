import json
import logging
from src.vacancies_save.abstract_vacancy_save import VacancySaver


class JsonSaver(VacancySaver):
    """ Класс для сохранения информации о вакансиях в JSON-файл"""

    def add_vacancy(self, save_vacancy):
        """Сохраняет в файл vacancies"""
        try:
            indexed_vacancies = {str(index): vacancy for index, vacancy in enumerate(save_vacancy, 1)}
            with open('vacancies.json', "w", encoding='utf-8') as file:
                json.dump(indexed_vacancies, file, indent=4, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Произошла ошибка при сохранении файла: {e}")

    def delete_vacancy(self, number_vacancy):
        """ Удаляет вакансию"""
        try:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            if str(number_vacancy) in data:
                del data[str(number_vacancy)]
                with open('vacancies.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                return True
            else:
                return False
        except FileNotFoundError:
            logging.error("Файл vacancies.json не найден.")
            return False
        except json.JSONDecodeError:
            logging.error("Ошибка декодирования JSON.")
            return False

    def get_vacancy(self, number_vacancy):
        """ Информация о конкретной вакансии"""
        try:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                vacancy_info = data.get(str(number_vacancy))
                return vacancy_info
        except FileNotFoundError:
            logging.error("Файл vacancies.json не найден.")
        except json.JSONDecodeError:
            logging.error("Ошибка декодирования JSON.")

    def get_all_vacancies(self):
        """Возвращает все сохраненные вакансии."""
        try:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            return list(data.values())
        except FileNotFoundError:
            logging.error("Файл vacancies.json не найден.")
            return []
        except json.JSONDecodeError:
            logging.error("Ошибка декодирования JSON.")
            return []
