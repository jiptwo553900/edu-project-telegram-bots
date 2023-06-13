from random import randint
from aiogram.types import Message


# Функция возвращающая случайное целое число от 1 до 100.
def get_random_num() -> int:
    return randint(1, 100)


# Функция проверяет соответствие ввода числу от 1 до 100.
def if_num_filter(msg: Message) -> bool:
    try:
        return int(msg.text) in range(1, 101)  # type: ignore
    except:
        return False


if __name__ == "__main__":
    pass
