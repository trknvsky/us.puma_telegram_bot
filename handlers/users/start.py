from aiogram.dispatcher.filters import CommandStart
from utils.db_api.db_commands import DBCommands
from loader import dp, bot
from aiogram import types

data = DBCommands()


@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    user = await data.add_new_user()
    count_users = await data.count_users()

    text = ("Hello, {}!!\n"
            "Tap /items to show menu\n").format(message.from_user.first_name)

    await bot.send_message(chat_id, text)





