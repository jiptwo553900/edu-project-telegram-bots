from config import *
from number_game_texts import *
from number_game_data import *
from number_game_tools import *

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message
from time import sleep

# Создание объектов бота, диспетчера.
bot = Bot(API_TOKEN)
dp = Dispatcher()


# Обработка команды /start.
@dp.message(Command(commands="start"))
async def process_start_command(msg: Message):
    await msg.answer(greet_msg)
    # Если игрок новый, создаем экземпляр класса в словаре 'gamers'
    if msg.from_user.id not in gamers:
        gamers[msg.from_user.id] = Gamer()


# Обработка команды /help.
@dp.message(Command(commands="help"))
async def process_help_command(msg: Message):
    await msg.answer(rules_msg)


# Обработка команды /stat.
@dp.message(Command(commands="stat"))
async def process_stat_command(msg: Message):
    await msg.answer(stat_msg.format(
        gamers[msg.from_user.id].total_games,
        gamers[msg.from_user.id].wins
    ))


# Обработка команды /cancel.
@dp.message(Command(commands="cancel"))
async def process_cancel_command(msg: Message):
    if gamers[msg.from_user.id].in_game:
        await msg.answer(cancel_game_msg)
        gamers[msg.from_user.id].in_game = False
    else:
        await msg.answer(no_active_game_msg)
    sleep(1)
    await msg.answer(invite_msg)


# Обработка согласия на игру.
@dp.message(Text(FILTER_POSITIVE, ignore_case=True))
async def process_positive_answer(msg: Message):
    if not gamers[msg.from_user.id].in_game:
        gamers[msg.from_user.id].in_game = True
        gamers[msg.from_user.id].secret_number = get_random_num()
        gamers[msg.from_user.id].attempts = ATTEMPTS
        await msg.answer(start_game_msg.format(
            gamers[msg.from_user.id].attempts
        ))
    else:
        await msg.answer(wrong_input_till_game)


# Обработка отказа от игры.
@dp.message(Text(FILTER_NEGATIVE, ignore_case=True))
async def process_negative_answer(msg: Message):
    if not gamers[msg.from_user.id].in_game:
        await msg.answer(invite_msg)
    else:
        await msg.answer(wrong_input_till_game)


# Обработка отправки чисел от 1 до 100.
@dp.message(if_num_filter)
async def process_num_answer(msg: Message):
    number = int(msg.text)  # type: ignore
    if gamers[msg.from_user.id].in_game:
        if gamers[msg.from_user.id].attempts == 0:
            gamers[msg.from_user.id].in_game = False
            gamers[msg.from_user.id].total_games += 1
            await msg.answer(no_more_attempts_msg.format(
                gamers[msg.from_user.id].secret_number
            ))
            sleep(1)
            await msg.answer(invite_msg)
        elif number > gamers[msg.from_user.id].secret_number:
            gamers[msg.from_user.id].attempts -= 1
            await msg.answer(num_is_lower_msg.format(
                gamers[msg.from_user.id].attempts
            ))
        elif number < gamers[msg.from_user.id].secret_number:
            gamers[msg.from_user.id].attempts -= 1
            await msg.answer(num_is_bigger_msg.format(
                gamers[msg.from_user.id].attempts
            ))
        else:
            gamers[msg.from_user.id].in_game = False
            gamers[msg.from_user.id].wins += 1
            gamers[msg.from_user.id].total_games += 1
            await msg.answer(win_msg)
            sleep(1)
            await msg.answer(invite_msg)


# Обработка всех других сообщений
@dp.message()
async def process_other_answers(msg: Message):
    if gamers[msg.from_user.id].in_game:
        await msg.answer(wrong_input_till_game)
    else:
        await msg.answer(wrong_input_no_game)
        sleep(1)
        await msg.answer(invite_msg)


if __name__ == '__main__':
    print("Bot started!")
    dp.run_polling(bot)
    print(gamers)
