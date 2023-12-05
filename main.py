from src.api.hh_api import HeadHunterApi
from src.api.superjob_api import SuperJobApi
from src.utils.conversion import *
from src.vacancies_save.json_saver import JsonSaver


# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    vacancies = []
    search_query = input("Привет!\n"
                         "Я представляю собой программу для поиска вакансий на платформах HeadHunter и SuperJob.\n"
                         "Пожалуйста, введите ваш поисковый запрос: ")
    search_platforms = input("Выберите платформу (HH - HeadHunter, SJ - SuperJob, Enter - все платформы): ")
    hh_api = HeadHunterApi()
    sj_api = SuperJobApi()
    if search_platforms.lower() == "hh":
        vacancies.extend(convert_to_vacancies(hh_api.get_vacancies(search_query), 'hh'))
    elif search_platforms.lower() == "sj":
        vacancies.extend(convert_to_vacancies(sj_api.get_vacancies(search_query), 'sj'))
    else:
        vacancies.extend(convert_to_vacancies(hh_api.get_vacancies(search_query), 'hh'))
        vacancies.extend(convert_to_vacancies(sj_api.get_vacancies(search_query), 'sj'))

    sorted_vacancies = sorted(vacancies)
    vacancies_dicts = [convert_vacancy_to_dict(vac, idx + 1) for idx, vac in enumerate(sorted_vacancies)]

    json_saver = JsonSaver()
    json_saver.add_vacancy(vacancies_dicts)

    for index, vacancy in enumerate(sorted_vacancies, start=1):
        print(f"{index}. Вакансия: {vacancy.name}, Зарплата: {vacancy.salary}")

    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    #
    # if not filtered_vacancies:
    #     print("Нет вакансий, соответствующих заданным критериям.")
    #     return
    #
    # sorted_vacancies = sort_vacancies(filtered_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
