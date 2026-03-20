from enum import Enum

class PRIORITIES(Enum):
    COMPLETED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EXTRA_HIGH = 4

READY_VARIANTS = ["готово", "выполнено", "завершено", "complete", "ready", "done"]
