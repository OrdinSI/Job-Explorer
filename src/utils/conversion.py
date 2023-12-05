from src.vacancy.vacancy import Vacancy


def convert_to_vacancies(vacancies_data, platform):
    vacancies = []
    if platform == "hh":
        for v in vacancies_data.get('items', []):
            salary_info = v.get('salary')
            salary = salary_info.get("from") if salary_info else None
            salary = salary if salary is not None and salary != 0 else "Не указана"
            snippets = v.get('snippet') or {}
            vacancies.append(Vacancy(
                name=v.get('name', ''),
                area=v.get('area').get('name'),
                url=v.get('alternate_url', ''),
                salary=salary,
                description=snippets.get('requirement', '')
            ))
    elif platform == "sj":
        for v in vacancies_data.get('objects', []):
            salary = v.get('payment_from')
            salary = salary if salary is not None and salary != 0 else "Не указана"
            vacancies.append(Vacancy(
                name=v.get('profession', ''),
                area=v.get('town').get('title'),
                url=v.get('link', ''),
                salary=salary,
                description=v.get('candidat', '')
            ))
    return vacancies


def convert_vacancy_to_dict(vacancy, index):
    return {
        "id": index,
        "name": vacancy.name,
        "url": vacancy.url,
        "area": vacancy.area,
        "salary": vacancy.salary,
        "description": vacancy.description
    }
