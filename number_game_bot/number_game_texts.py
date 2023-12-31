from number_game_data import *

greet_msg = ("Привет! \n"
             "Давайте сыграем в игру 'Угадай число'? \n\n"
             "Чтобы получить правила игры и список доступных "
             "команд - отправьте команду /help")

rules_msg = (f"Правила игры: \n\n"
             f"Я загадываю число от 1 до 100, "
             f"а вам нужно его угадать \n"
             f"У вас есть {ATTEMPTS} попыток \n\n"
             f"Доступные команды: \n"
             f"/help - правила игры и список команд \n"
             f"/cancel - выйти из игры \n"
             f"/stat - посмотреть статистику \n\n"
             f"Давай сыграем?")

stat_msg = "Игр сыграно: {} \nПобед всего: {}"

cancel_game_msg = "Вы вышли из игры."

no_active_game_msg = ("А мы с вами и так не играем :( \n"
                      "Может, сыграем разок?")

invite_msg = ("Если хотите сыграть - отправьте: 'Да', "
              "'Давай', 'Сыграем', 'Игра', 'Играть' или "
              "'Хочу играть'")

start_game_msg = ("Ура! \n"
                  "Я загадал число от 1 до 100. "
                  "Попробуйте угадать! \n"
                  "У ваc {} попыток!")

wrong_input_till_game = ("Пока мы играем в игру я могу "
                         "реагировать только на числа от "
                         "1 до 100 и на команды /cancel и /stat")

wrong_input_no_game = ("Я довольно ограниченный бот, давайте "
                       "просто сыграем в игру?")

no_more_attempts_msg = ("К сожалению, у вас больше не осталось попыток. "
                        "Вы проиграли :( \n\n"
                        "Мое число было {} \n\n"
                        "Давайте сыграем еще?")

num_is_lower_msg = "Мое число меньше. \nПопыток осталось: {}"
num_is_bigger_msg = "Мое число больше. \nПопыток осталось: {}"

win_msg = "Ура!!! Вы угадали число! \n\nМожет, сыграем еще?"

if __name__ == "__main__":
    pass
