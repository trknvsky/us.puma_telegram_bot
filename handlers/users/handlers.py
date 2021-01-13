from aiogram import types
from asyncpg import Connection, Record
from loader import dp, bot, db
from asyncpg.exceptions import UniqueViolationError


class DBCommands:
    pool: Connection = db
    ADD_NEW_USER = "INSERT INTO users (chat_id, username, full_name) VALUES ($1, $2, $3) RETURNING id"
    COUNT_USERS = "SELECT COUNT(*) FROM users"
    GET_ID  = "SELECT id FROM users WHERE chat_id = $1"

    async def add_new_user(self):
        user = types.User.get_current()
        chat_id = user.id
        full_name = user.full_name
        username = user.username
        args = chat_id, username, full_name
        command = self.ADD_NEW_USER

        try:
            record_id = await self.pool.fetchval(command, *args)
            return record_id
        except UniqueViolationError:
            pass

    async def count_users(self):
        record: Record = await self.pool.fetchval(self.COUNT_USERS)
        return record

    async def get_id(self):
        command = self.GET_ID
        user_id = types.User.get_current().id
        return await self.pool.fetchval(command, user_id)


data = DBCommands()


@dp.message_handler(commands=['start'])
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    id = await data.add_new_user()
    count_users = await data.count_users()
    if not id:
        id = await data.get_id()
    else:
        text = "Записано в базу данных"
    text += f"""
Сейчас в базе {count_users} человек!

"""
    await bot.send_message(chat_id, text)



