import pytest  # type: ignore[import-not-found]
from datetime import datetime

from src.models.task import Task
from src.models.descriptors import IdDescriptor
from src.models.exceptions import IdException

def test_id_get():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert test_task.id == "test1"
    assert type(Task.id) is IdDescriptor

def test_id_set():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(IdException):
        test_task.id = "id1"

def test_id_incorrect_value():
    with pytest.raises(IdException):
        Task("    ", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(IdException):
        Task(1, "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))


def test_id_del():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(IdException):
        del test_task.id
