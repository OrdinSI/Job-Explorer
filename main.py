from src.utils.colors import Colors
import logging
from src.api.hh_api import HeadHunterApi
from src.api.superjob_api import SuperJobApi
from src.utils.config import *
from src.utils.conversion import *
from src.utils.filter import *
from src.vacancies_save.json_saver import JsonSaver
from src.utils.messages import *

logging.basicConfig(
    #filename='job_explorer.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(module)s:  [%(funcName)s] %(message)s'
)


def user_interaction():
    """ Основная функция для взаимодействия с пользователем"""
    vacancies = []
    Colors.print_magenta(GREETING)
    search_query = Colors.input_cyan(ENTER_QUERY)

    # Выбор платформы
    search_platforms = Colors.input_cyan(ENTER_PLATFORM)
    hh_api = HeadHunterApi()
    sj_api = SuperJobApi()
    if search_platforms.lower() == "hh":
        vacancies.extend(convert_to_vacancies(hh_api.get_vacancies(search_query), 'hh'))
    elif search_platforms.lower() == "sj":
        vacancies.extend(convert_to_vacancies(sj_api.get_vacancies(search_query), 'sj'))
    else:
        vacancies.extend(convert_to_vacancies(hh_api.get_vacancies(search_query), 'hh'))
        vacancies.extend(convert_to_vacancies(sj_api.get_vacancies(search_query), 'sj'))

    # Сортировка по зарплате и сохранение в файл
    sorted_vacancies = sorted(vacancies)
    vacancies_dicts = [convert_vacancy_to_dict(vac, idx + 1) for idx, vac in enumerate(sorted_vacancies)]

    json_saver = JsonSaver()
    json_saver.add_vacancy(vacancies_dicts)

    while True:
        # Предлагаем пользователю выбор действия
        Colors.print_magenta(PRINT_CHOICE)
        choice = Colors.input_cyan(INPUT_CHOICE)

        if choice == "1":
            # Выводим список вакансий
            vacancies_dicts = json_saver.get_all_vacancies()
            for index, vacancy in enumerate(vacancies_dicts, start=1):
                Colors.print_blue(PRINT_VACANCIES.format(index, vacancy.get('name'), vacancy.get('salary')))
                continue

        if choice == "2":
            # Выводим информацию по конкретной вакансии по номеру
            number_vacancy = Colors.input_cyan(ENTER_NUMBER_VACANCY)

            vacancy_info = json_saver.get_vacancy(number_vacancy)
            if vacancy_info:
                for key, value in vacancy_info.items():
                    name = KEYS_TO_NAMES.get(key, key)
                    Colors.print_blue(PRINT_VACANCY.format(name, value))
            else:
                Colors.print_red(NOT_VACANCY_NUMBER.format(number_vacancy))

        if choice == "3":
            # Фильтр по зарплате
            min_salary = Colors.input_cyan(ENTER_SALARY)
            if min_salary:
                min_salary = int(min_salary)
                vacancies_dicts = filter_by_salary(vacancies_dicts, min_salary)
                for vacancy in vacancies_dicts:
                    Colors.print_blue(PRINT_VACANCIES.format(vacancy['id'], vacancy['name'], vacancy['salary']))

        if choice == "4":
            # Поиск по ключевому слову в описании
            keyword = Colors.input_cyan(ENTER_KEYWORD)
            if keyword:
                vacancies_dicts = filter_by_keyword(vacancies_dicts, keyword)
            if not vacancies_dicts:
                Colors.print_red(NOT_VACANCY_KEYWORD)
            else:
                for vacancy in vacancies_dicts:
                    Colors.print_blue(PRINT_VACANCIES.format(vacancy['id'], vacancy['name'], vacancy['salary']))

        if choice == "5":
            # Позволяем пользователю удалять вакансии из файла
            delete_vacancy_number = Colors.input_cyan(ENTER_DELETE_VACANCY)
            if delete_vacancy_number:
                if json_saver.delete_vacancy(delete_vacancy_number):
                    Colors.print_red(CONFIRMATION_DELETE_VACANCY.format(delete_vacancy_number))
                    vacancies_dicts = json_saver.get_all_vacancies()
                    for index, vacancy in enumerate(vacancies_dicts, start=1):
                        Colors.print_blue(PRINT_VACANCIES.format(index, vacancy.get('name'), vacancy.get('salary')))
                else:
                    Colors.print_red(ERROR_DELETE_VACANCY.format(delete_vacancy_number))

        if choice == "6":
            Colors.print_magenta(GOODBYE_MESSAGE)
            break


if __name__ == "__main__":
    user_interaction()
