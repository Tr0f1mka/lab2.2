import pytest  # type: ignore[import-not-found]
from datetime import datetime

from src.models.task import Task
from src.models.descriptors import StatusDescriptor
from src.models.exceptions import StatusException

def test_status_get():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert test_task.status == "In progress"
    assert type(Task.status) is StatusDescriptor

def test_status_set():

    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    test_task.status = "done"
    assert test_task.status == "done"

def test_status_incorrect_value():
    with pytest.raises(StatusException):
        Task("test1", "Сделать эту лабораторную работу", 3, 34, datetime(2026, 3, 18))


def test_status_del():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(StatusException):
        del test_task.status
