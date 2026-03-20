from dataclasses import dataclass
from datetime import datetime

from src.models.descriptors import (IdDescriptor,
                                    DescriptionDescriptor,
                                    PriorityDescriptor,
                                    StatusDescriptor,
                                    IsReadyDescriptor)
from src.models.exceptions import CreateTimeException


@dataclass
class Task:
    """
    Класс задачи
    """

    id = IdDescriptor()
    description = DescriptionDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()
    is_ready = IsReadyDescriptor()

    @property
    def create_time(self):
        """
        Геттер для create_time
        """
        return self._date

    @create_time.setter
    def create_time(self, value):
        """
        Сеттер для create_time
        """
        if hasattr(self, "_date"):
            raise CreateTimeException("Change date")
        if not isinstance(value, datetime):
            raise CreateTimeException("Incorrect type")
        self._date = value

    def __init__(self, id: str, description: str, priority: int, status: str, create_time: datetime):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.create_time = create_time
