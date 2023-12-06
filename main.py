from colorama import Fore, Style

from src.api.hh_api import HeadHunterApi
from src.api.superjob_api import SuperJobApi
from src.utils.config import *
from src.utils.conversion import *
from src.utils.filter import *
from src.vacancies_save.json_saver import JsonSaver


def user_interaction():
    """ Основная функция для взаимодействия с пользователем"""
    vacancies = []
    print(
        f"{Fore.MAGENTA}Привет!\nЯ представляю собой программу для поиска вакансий на платформах HeadHunter и SuperJob.{Style.RESET_ALL}")
    search_query = input(f"{Fore.CYAN}Пожалуйста, введите ваш поисковый запрос: {Style.RESET_ALL}")

    # Выбор платформы
    search_platforms = input(
        f"{Fore.CYAN}Выберите платформу (HH - HeadHunter, SJ - SuperJob, Enter - все платформы): {Style.RESET_ALL}")
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
        print(f"""{Fore.MAGENTA}
        Выберите действие:
        1. Посмотреть весь список вакансий.
        2. Просмотреть информацию о вакансии.
        3. Фильтр по зарплате.
        4. Поиск по ключевому слову в описании.
        5. Удалить вакансию.
        6. Выход.
        {Style.RESET_ALL}""")

        choice = input(f"{Fore.CYAN}Введите номер действия: {Style.RESET_ALL}")

        if choice == "1":
            # Выводим список вакансий
            vacancies_dicts = json_saver.get_all_vacancies()
            for index, vacancy in enumerate(vacancies_dicts, start=1):
                print(
                    f"{Fore.BLUE}{index}. Вакансия: {vacancy.get('name')}, Зарплата: {vacancy.get('salary')}{Style.RESET_ALL}")
                continue

        if choice == "2":
            # Выводим информацию по конкретной вакансии по номеру
            number_vacancy = input(
                f"{Fore.CYAN}Введите номер вакансии для отображения информации по ней: {Style.RESET_ALL}")

            vacancy_info = json_saver.get_vacancy(number_vacancy)
            if vacancy_info:
                for key, value in vacancy_info.items():
                    name = KEYS_TO_NAMES.get(key, key)
                    print(f"{Fore.BLUE}{name}: {value}")
            else:
                print(f"{Fore.RED}Вакансия с номером {number_vacancy} не найдена.{Style.RESET_ALL}")

        if choice == "3":
            # Фильтр по зарплате
            min_salary = input(
                f"{Fore.CYAN}Введите минимальную желаемую зарплату (или оставьте пустым, чтобы не фильтровать): {Style.RESET_ALL}")
            if min_salary:
                min_salary = int(min_salary)
                vacancies_dicts = filter_by_salary(vacancies_dicts, min_salary)
                for index, vacancy in enumerate(vacancies_dicts, start=1):
                    print(
                        f"{Fore.BLUE}{index}. Вакансия: {vacancy.get('name')}, Зарплата: {vacancy.get('salary')}{Style.RESET_ALL}")

        if choice == "4":
            # Поиск по ключевому слову в описании
            keyword = input(
                f"{Fore.CYAN}Введите ключевое слово для поиска в описании (или оставьте пустым, чтобы не фильтровать): {Style.RESET_ALL}")
            if keyword:
                vacancies_dicts = filter_by_keyword(vacancies_dicts, keyword)
            if not vacancies_dicts:
                print(f"{Fore.RED}По вашим критериям не найдено ни одной вакансии.{Style.RESET_ALL}")
            else:
                for index, vacancy in enumerate(vacancies_dicts, start=1):
                    print(
                        f"{Fore.BLUE}{index}. Вакансия: {vacancy.get('name')}, Зарплата: {vacancy.get('salary')}{Style.RESET_ALL}")

        if choice == "5":
            # Позволяем пользователю удалять вакансии из файла
            delete_vacancy_number = input(
                f"{Fore.CYAN}Введите номер вакансии для удаления (или нажмите Enter, чтобы продолжить): {Style.RESET_ALL}")
            if delete_vacancy_number:
                if json_saver.delete_vacancy(delete_vacancy_number):
                    print(f"{Fore.RED}Вакансия с номером {delete_vacancy_number} удалена.{Style.RESET_ALL}")
                    vacancies_dicts = json_saver.get_all_vacancies()
                    for index, vacancy in enumerate(vacancies_dicts, start=1):
                        print(
                            f"{Fore.BLUE}{index}. Вакансия: {vacancy.get('name')}, Зарплата: {vacancy.get('salary')}{Style.RESET_ALL}")
                else:
                    print(
                        f"{Fore.RED}Не удалось удалить вакансию с номером {delete_vacancy_number}. Возможно, она уже была удалена.{Style.RESET_ALL}")

        if choice == "6":
            print(f"{Fore.MAGENTA}Всего доброго!{Style.RESET_ALL}")
            break


if __name__ == "__main__":
    user_interaction()
