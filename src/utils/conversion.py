from src.vacancy.vacancy import Vacancy


def convert_to_vacancies(vacancies_data, platform):
    vacancies = []
    if platform == "hh":
        for v in vacancies_data.get('items', []):
            salary_info = v.get('salary')
            salary = salary_info.get("from") if salary_info else None
            salary = salary if salary is not None and salary != 0 else "Не указана"
            snippets_info = v.get('snippet')
            snippet = snippets_info.get('requirement') if snippets_info else None
            snippet = snippet if snippet is not None else "Не указано"
            area_info = v.get('area')
            area = area_info.get('name') if area_info else None
            area = area if area is not None else "Не указано"
            vacancies.append(Vacancy(
                name=v.get('name', "Не указана"),
                area=area,
                url=v.get('alternate_url', "Не указан"),
                salary=salary,
                description=snippet
            ))
    elif platform == "sj":
        for v in vacancies_data.get('objects', []):
            salary = v.get('payment_from')
            salary = salary if salary is not None and salary != 0 else "Не указана"
            area_info = v.get('town')
            area = area_info.get('title') if area_info else None
            area = area if area is not None else "Не указано"
            vacancies.append(Vacancy(
                name=v.get('profession', "Не указана"),
                area=area,
                url=v.get('link', "Не указан"),
                salary=salary,
                description=v.get('candidat', "Не указано")
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
