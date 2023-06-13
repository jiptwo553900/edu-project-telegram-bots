from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import *
from pprint import pp

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(msg: Message):
    await msg.answer(
        "Привет! Меня зовут Echo-Bot! Напиши мне что-нибудь!"
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(msg: Message):
    await msg.answer(
        "Напиши мне что-нибудь, и я напишу тебе то же самое в ответ!"
    )


"""
# Хэндлер обрабатывает отправку фото.
@dp.message(F.photo)
async def echo_photo(msg: Message):
    pp(msg.dict())
    await msg.answer_photo(msg.photo[0].file_id, caption=msg.caption)


# Хэндлер обрабатывает отправку видео.
@dp.message(F.video)
async def echo_video(msg: Message):
    pp(msg.dict())
    await msg.answer_video(msg.video.file_id, caption=msg.caption)


# Хэндлер обрабатывает отправку стикера.
@dp.message(F.sticker)
async def echo_video(msg: Message):
    pp(msg.dict())
    await msg.answer_sticker(msg.sticker.file_id, caption=msg.caption)


# Хэндлер обрабатывает остальные сообщения.
@dp.message()
async def send_echo(msg: Message):
    pp(msg.dict())
    await msg.reply(text=msg.text)
"""


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message)
    print(message.json(indent=4, exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)
