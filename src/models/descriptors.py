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

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> str:
        """
        Геттер для ID
        """
        logger.info("GET ID")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: str) -> None:
        """
        Сеттер для ID
        """
        logger.info(f"SET ID: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise IdException("ID есть только в существуюшей задаче")
        if hasattr(instance, self.private_name):
            logger.error("ID already set")
            raise IdException("Нельзя менять ID задачи")
        if not isinstance(value, str) or value.strip() == "":
            logger.error("Incorrect value")
            raise IdException("Некорректный ID задачи")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для ID
        """
        logger.error("DEL ID")
        raise IdException("Нельзя удалять ID задачи")


class DescriptionDescriptor:
    """
    Дескриптор описания задачи: запрещает изменения
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> str:
        """
        Геттер для description
        """
        logger.info("GET DESCRIPTION")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: str) -> None:
        """
        Сеттер для description
        """
        logger.info(f"SET desription: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise DescriptionException("Description есть только в существуюшей задаче")
        if hasattr(instance, self.private_name):
            logger.error("Description already set")
            raise DescriptionException("Нельзя менять описание задачи")
        if not isinstance(value, str) or value.strip() == "":
            logger.error("Incorrect value")
            raise DescriptionException("Некорректное описание задачи")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для description
        """
        logger.error("DEL description")
        raise DescriptionException("Нельзя удалять описание задачи")


class PriorityDescriptor:
    """
    Дескриптор приоритета: можно смотреть и менять
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> int:
        """
        Геттер для priority
        """
        logger.info("GET priority")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: int) -> None:
        """
        Сеттер для priority
        """
        logger.info(f"SET priority: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise PriorityException("Priority есть только в существуюшей задаче")
        if not isinstance(value, int):
            logger.error("Incorrect type value")
            raise PriorityException("Priority задачи должно быть числом")
        if value not in PRIORITIES:
            logger.error("Incorrect value")
            raise PriorityException("Priority должно быть от 0 до 4")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для priority
        """
        logger.error("DEL priority")
        raise PriorityException("Нельзя удалять приоритет задачи")


class StatusDescriptor:
    """
    Дескриптор статуса: можно смотреть и менять
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> str:
        """
        Геттер для status
        """
        logger.info("GET status")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: str) -> None:
        """
        Сеттер для status
        """
        logger.info(f"SET status: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise StatusException("Status есть только в существуюшей задаче")
        if not isinstance(value, str):
            logger.error("Incorrect type value")
            raise StatusException("Status задачи должно быть строкой")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для status
        """
        logger.error("DEL status")
        raise StatusException("Нельзя удалять статус задачи")


class IsReadyDescriptor:
    """
    Non-data дескриптор вычисления готовности задачи
    """

    def __get__(self, instance: "Task", cls: "type[Task]") -> bool:
        """
        Геттер для is_ready
        """
        logger.info("GET is_ready")
        if instance is None:
            return self
        return instance.status.lower() in READY_VARIANTS
