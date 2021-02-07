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

    text = ("Приветствую вас {}!!\n"
            "Сейчас в базе {} человек!\n").format(user.username, count_users)

    await bot.send_message(chat_id, text)





