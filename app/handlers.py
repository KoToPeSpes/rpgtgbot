from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
import sqlite3

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    print(message.from_user.first_name, message.from_user.id)
    await message.answer("sosal da")
