# Educational project. Simple Telegram bots.
**Учебный проект. Простые Телеграм-боты.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

## Installation 🛠️
1. Clone the repository in your folder git clone `https://github.com/jiptwo553900/edu-project-telegram-bots.git`
2. Rename `config.example` in [📁/echo_bot/](/echo_bot/) or [📁/number_game_bot/](/number_game_bot/) directories to `config`
3. Set your bot token in the token field in `config`
4. For the [📁/cat_bot/](/cat_bot/) set your token to `BOT_TOKEN`variable in [/cat_bot/main.py](/cat_bot/main.py)
5. Install need libraries `pip3 install -r requirements.txt`
6. Run bots with `main.py` in [📁/cat_bot/](/cat_bot/), [📁/echo_bot/](/echo_bot/) or [📁/number_game_bot/](/number_game_bot/)

## Cat Bot 🐱
**Описание:** Простейший однофайловый бот, в ответ на апдейт отправляет картинку с котиком.\
**Расположение:** [📁/cat_bot/](/cat_bot/)\
**Структура:** нет

## Echo Bot 🔊
**Описание:** Простой однофайловый бот, на сообщение отправляет его же в ответ. 
Умеет реагировать на команды `\start` и `\help`\
**Расположение:** [📁/echo_bot/](/echo_bot/)\
**Структура:**
```
├── 📁 echo_bot
│   ├── 📄 config    # Токен берется отсюда
│   └── 📄 main.py
```

## NumberGame Bot
**Описание:** Простой бот с элементарной структурой, который умеет играть 
в "Угадай число"\
**Расположение:** [📁/number_game_bot/](/number_game_bot/)\
**Структура:**
```
├── 📁 number_game_bot
│   ├── 📄 number_game_data.py   # Классы, константы
│   ├── 📄 number_game_texts.py  # Лексикон
│   ├── 📄 number_game_tools.py  # Вспомогательные функции
│   ├── 📄 config                # Токен берется отсюда
│   └── 📄 main.py               # Точка входа. Хэндлеры.
```