import pytest  # type: ignore[import-not-found]
from datetime import datetime

from src.models.task import Task
from src.models.exceptions import CreateTimeException

def test_create_time_get():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert test_task.create_time == datetime(2026, 3, 18)

def test_create_time_set():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    with pytest.raises(CreateTimeException):
        test_task.create_time = datetime(1, 1, 1)
    with pytest.raises(CreateTimeException):
        test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", 23)
