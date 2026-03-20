import pytest  # type: ignore[import-not-found]     # noqa: F401
from datetime import datetime

from src.models.task import Task
from src.models.descriptors import IsReadyDescriptor

def test_is_ready_get():
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "In progress", datetime(2026, 3, 18))
    assert not test_task.is_ready
    test_task = Task("test1", "Сделать эту лабораторную работу", 3, "Done", datetime(2026, 3, 18))
    assert test_task.is_ready
    assert type(Task.is_ready) is IsReadyDescriptor
