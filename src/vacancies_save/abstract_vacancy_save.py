from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Абстрактный класс для работы с вакансиями(сохранение, чтение, удаление)"""

    @abstractmethod
    def add_vacancy(self, save_vacancy):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
