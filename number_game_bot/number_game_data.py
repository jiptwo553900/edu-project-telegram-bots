from dataclasses import dataclass
from typing import Sequence


# Датакласс для хранения информации об игроке.
@dataclass()
class Gamer:
    in_game: bool = False
    secret_number: int = 0
    attempts: int = 0
    total_games: int = 0
    wins: int = 0


# Словарь для хранения данных игроков
gamers: dict[int, Gamer] = {}

# Количество попыток, доступных игроку в игре.
ATTEMPTS: int = 5

# Наборы для фильтрации апдейтов
FILTER_POSITIVE: Sequence[str] = ("Да", "Давай", "Сыграем", "Игра",
                                  "Играть", "Хочу играть")
FILTER_NEGATIVE: Sequence[str] = ("Нет", "Не", "Не хочу", "Не буду")

if __name__ == "__main__":
    pass
