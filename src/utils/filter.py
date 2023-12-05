def filter_by_salary(vacancies, min_salary):
    filtered_vacancies = []
    for vac in vacancies:
        salary = vac.get('salary')
        if salary and salary != "Не указана":
            if salary >= min_salary:
                filtered_vacancies.append(vac)
    return filtered_vacancies


def filter_by_keyword(vacancies, keyword):
    keyword_lower = keyword.lower()
    return [vac for vac in vacancies if keyword_lower in vac.get('description', '').lower()]