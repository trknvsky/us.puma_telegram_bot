import asyncio
from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.db_api.sql import create_db
from utils.notify_admins import on_startup_notify
from data.config import ADMINS
from loader import bot


async def on_startup(dispatcher):
    await asyncio.sleep(2)
    await create_db()
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
