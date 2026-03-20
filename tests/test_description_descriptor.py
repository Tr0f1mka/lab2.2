import pytest  # type: ignore[import-not-found]
from datetime import datetime

from src.models.task import Task
from src.models.descriptors import DescriptionDescriptor
from src.models.exceptions import DescriptionException

def test_description_get():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert test_task.description == "Сделать эту лабораторную работу"
    assert type(Task.description) is DescriptionDescriptor

def test_description_set():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(DescriptionException):
        test_task.description = "description1"

def test_description_incorrect_value():
    with pytest.raises(DescriptionException):
        Task("test1", "     ", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(DescriptionException):
        Task("test1", 34, 3, "In progress", datetime(2026, 3, 18))


def test_description_del():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(DescriptionException):
        del test_task.description
