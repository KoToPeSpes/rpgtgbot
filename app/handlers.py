from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
import sqlite3
from .game import Inventory

router = Router()


def init_db():
    connection = sqlite3.connect("players.db", timeout=30.0)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Players (
            userid PRIMARY KEY NOT NULL,
            level INTEGER NOT NULL DEFAULT 1
        )
    ''')
    connection.commit()
    connection.close()

init_db()


@router.message(CommandStart())
async def cmd_start(message: Message):
    print(message.from_user.first_name, message.from_user.id)
    await message.answer("дароу, что бы начать игру пропиши 'В приключение!'")


@router.message(F.text == "В приключение!")
async def create_player(message: Message):
    print("zafiksiroval!")
    user_id = message.from_user.id
    connection = sqlite3.connect("players.db", timeout=30.0)
    cursor = connection.cursor()
    cursor.execute("INSERT OR IGNORE INTO Players (userid) VALUES (?)", (user_id,))
    connection.commit()
    connection.close()
    await message.answer("Понял! Занес тебя в дб")


@router.message(F.text == "Инвентарь")
async def check_inventory(message: Message):
    print("proveril inv")
    user_id = message.from_user.id
    connection = sqlite3.connect("players.db", timeout=30.0)
    cursor = connection.cursor()
    cursor.execute("SELECT level FROM Players WHERE userid = ?", (user_id,))
    level = cursor.fetchone()[0]
    connection.close()
    await message.answer(f"@{message.from_user.username}, твой уровень: {level}")