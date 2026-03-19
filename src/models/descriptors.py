from typing import TYPE_CHECKING

from src.models.logger import logger
from src.models.exceptions import (IdException,
                                   DescriptionException,
                                   PriorityException,
                                   StatusException)
from src.constants import PRIORITIES, READY_VARIANTS
if TYPE_CHECKING:
    from src.models.task import Task


class IdDescriptor:
    """
    Дескриптор ID задачи: запрещает изменения
    """

    def __get__(self, instance: "Task", cls: "type[Task]"):
        """
        Геттер для ID
        """
        logger.info("GET ID")
        if instance is None:
            return self
        return self.id
    
    def __set__(self, instance: "Task", value: str):
        """
        Сеттер для ID
        """
        logger.info(f"SET ID: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise IdException("ID есть только в существуюшей задаче")
        if hasattr(instance, "id"):
            logger.error("Not defined ID-field")
            raise IdException("Нельзя менять ID задачи")
        if not isinstance(value, str):
            logger.error("Incorrect type value")
            raise IdException("ID задачи должно быть строкой")
        self.id = value
        logger.info("SUCCES")
    
    def __delete__(self, instance: "Task"):
        """
        Делитер для ID
        """
        logger.error("DEL ID")
        raise IdException("Нельзя удалять ID задачи")   


class DescriptionDescriptor:
    """
    Дескриптор описания задачи: запрещает изменения
    """

    def __get__(self, instance: "Task", cls: "type[Task]"):
        """
        Геттер для description
        """
        logger.info("GET DESCRIPTION")
        if instance is None:
            return self
        return self.description
    
    def __set__(self, instance: "Task", value: str):
        """
        Сеттер для description
        """
        logger.info(f"SET desription: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise DescriptionException("description есть только в существуюшей задаче")
        if hasattr(instance, "description"):
            logger.error("Not defined description-field")
            raise DescriptionException("Нельзя менять DESCRIPTION задачи")
        if not isinstance(value, str):
            logger.error("Incorrect type value")
            raise DescriptionException("description задачи должно быть строкой")
        self.description = value
        logger.info("SUCCES")

    def __delete__(self, instance: "Task"):
        """
        Делитер для description
        """
        logger.error("DEL description")
        if instance is None:
            raise DescriptionException("Описание есть только в существующей задаче")
        if hasattr(instance, "description"):
            raise DescriptionException("Нельзя удалять описание задачи")


class PriorityDescriptor:
    """
    Дескриптор приоритета: можно смотреть и менять
    """

    def __get__(self, instance: "Task", cls: "type[Task]"):
        """
        Геттер для priority
        """
        logger.info("GET priority")
        if instance is None:
            return self
        return self.priority
    
    def __set__(self, instance: "Task", value: int):
        """
        Сеттер для priority
        """
        logger.info(f"SET priority: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise PriorityException("priority есть только в существуюшей задаче")
        if not isinstance(value, int):
            logger.error("Incorrect type value")
            raise PriorityException("priority задачи должно быть строкой")
        if value not in PRIORITIES:
            logger.error("Incorrect value")
            raise PriorityException("priority должно быть от 0 до 4")
        self.priority = value
        logger.info("SUCCES")
    
    def __delete__(self, instance: "Task"):
        """
        Делитер для priority
        """
        logger.error("DEL priority")
        if instance is None:
            raise PriorityException("Приоритет есть только в существующей задаче")
        if hasattr(instance, "priority"):
            raise PriorityException("Нельзя удалять приоритет задачи")


class StatusDescriptor:
    """
    Дескриптор статуса: можно смотреть и менять
    """

    def __get__(self, instance: "Task", cls: "type[Task]"):
        """
        Геттер для status
        """
        logger.info("GET status")
        if instance is None:
            return self
        return self.status
    
    def __set__(self, instance: "Task", value: str):
        """
        Сеттер для status
        """
        logger.info(f"SET status: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise StatusException("status есть только в существуюшей задаче")
        if not isinstance(value, str):
            logger.error("Incorrect type value")
            raise StatusException("status задачи должно быть строкой")
        self.status = value
        logger.info("SUCCES")
    
    def __delete__(self, instance: "Task"):
        """
        Делитер для status
        """
        logger.error("DEL status")
        if instance is None:
            raise StatusException("Статус есть только в существующей задаче")
        if hasattr(instance, "status"):
            raise StatusException("Нельзя удалять статус задачи")


class IsReadyDescriptor:
    """
    Non-data дескриптор вычисления готовности задачи
    """

    def __get__(self, instance: "Task", cls: "type[Task]"):
        """
        Геттер для is_ready
        """
        logger.info("GET is_ready")
        if instance is None:
            return self
        return instance.status.lower() in READY_VARIANTS