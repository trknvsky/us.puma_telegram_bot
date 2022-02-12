import asyncio
from aiogram import executor
from utils.notify_admins import on_startup_notify
from utils.db_api.database import create_db


async def on_startup(dp):
    await asyncio.sleep(5)
    # await create_db()
    await on_startup_notify(dp)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
