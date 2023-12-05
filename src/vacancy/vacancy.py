class Vacancy:
    """ Класс для работы с вакансиями"""

    def __init__(self, name: str, url: str, salary: [str, int, float], description: str) -> None:
        self.validate_data(name, url, salary, description)
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    @classmethod
    def validate_data(cls, name, url, salary, description):
        """ Метод для валидации данных"""
        if not isinstance(name, str) or not isinstance(url, str) or not isinstance(salary,
                                                                                   (str, int, float)) or not isinstance(
                description, str):
            raise ValueError("Некорректный формат данных")

        if not name or not url or not description:
            raise ValueError("Обязательные поля не заполнены")

    def __gt__(self, other):
        """ Метод для сортировки данных по зарплате от меньшего к большему"""
        if isinstance(other, Vacancy):
            if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float)):
                return self.salary > other.salary
            if isinstance(self.salary, (int, float)) and isinstance(other.salary, str):
                return False
            if isinstance(self.salary, str) and isinstance(other.salary, (int, float)):
                return True
            else:
                return True
        return NotImplemented

    def __repr__(self):
        return f"Vacancy(name={self.name}, url={self.url}, salary={self.salary}, description={self.description})"
