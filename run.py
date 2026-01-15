import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

import app.game as game_module
game_module.bot = bot

async def main():      # делаем бота
    dp.include_router(router)
    await dp.start_polling(bot)

print(BOT_TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("ВЫХОДЕМ...")