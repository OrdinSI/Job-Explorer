from src.api.hh_api import HeadHunterApi
from src.api.superjob_api import SuperJobApi


# Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    hh_vacancies = None
    sj_vacancies = None
    search_query = input("Привет!\n"
                         "Я представляю собой программу для поиска вакансий на платформах HeadHunter и SuperJob.\n"
                         "Пожалуйста, введите ваш поисковый запрос: ")
    search_platforms = input("Выберите платформу (HH - HeadHunter, SJ - SuperJob, Enter - все платформы): ")
    hh_api = HeadHunterApi()
    sj_api = SuperJobApi()
    if search_platforms.lower() == "hh":
        hh_vacancies = hh_api.get_vacancies(search_query)
    elif search_platforms.lower() == "sj":
        sj_vacancies = sj_api.get_vacancies(search_query)
    else:
        hh_vacancies = hh_api.get_vacancies(search_query)
        sj_vacancies = sj_api.get_vacancies(search_query)

    print(f"hh_vacancies: {hh_vacancies}")
    print(f"sj_vacancies: {sj_vacancies}")

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
