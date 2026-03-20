import pytest    # type: ignore[import-not-found]
from datetime import datetime

from src.models.task import Task
from src.models.descriptors import PriorityDescriptor
from src.models.exceptions import PriorityException

def test_priority_get():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert test_task.priority == 3
    assert type(Task.priority) is PriorityDescriptor

def test_priority_set():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    test_task.priority = 2
    assert test_task.priority == 2

def test_priority_incorrect_value():
    with pytest.raises(PriorityException):
        Task("test1", "Сделать эту лабораторную работу", "3", "In progress", datetime(2026, 3, 18))


def test_priority_del():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(PriorityException):
        del test_task.priority
