from datetime import datetime
from src.models.task import Task

"""
-------------------------
-------Точка входа-------
-------------------------
"""

def help() -> None:
    print("get_id - вывести ID задачи")
    print("set_id - изменить ID задачи")
    print("get_description - вывести описание задачи")
    print("set_description - изменить описание задачи")
    print("get_priority - вывести приоритет задачи")
    print("set_priority - изменить приоритет задачи")
    print("get_status - вывести статус задачи")
    print("set_status - изменить статус задачи")
    print("get_create_time - вывести время создания задачи")
    print("set_create_time - изменить время создания задачи")
    print("get_is_ready - вывести готовность задачи")
    print("help - сводка по командам")

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    task = Task("23mkg5", "Тестовая задача", 3, "fixing", datetime(1, 1, 1, 1, 1, 1))
    print("Для сводки по командам введите \"help\"")
    while ((cin := input("Введите команду: ")) != "exit"):
        try:
            match cin:
                case "get_id":
                    print(task.id)

                case "set_id":
                    val = input("Введите ID: ")
                    task.id = val

                case "get_description":
                    print(task.description)

                case "set_description":
                    val = input("Введите description: ")
                    task.description = val

                case "get_status":
                    print(task.status)

                case "set_status":
                    val = input("Введите status: ")
                    task.status = val

                case "get_priority":
                    print(task.priority)

                case "set_priority":
                    val_int = int(input("Введите priority: "))
                    task.priority = val_int

                case "get_create_time":
                    date = task.create_time
                    print(date.year, date.month, date.day)

                case "set_create_time":
                    year = int(input("Введите год: "))
                    month = int(input("Введите месяц: "))
                    day = int(input("Введите день: "))
                    task.create_time = datetime(year, month, day)

                case "get_is_ready":
                    print(task.is_ready)

                case "help":
                    help()

                case _:
                    print("Некорректный ввод")

        except Exception:
            print("Error: try again and watch logs in debug.log")



if __name__ == "__main__":
    main()
