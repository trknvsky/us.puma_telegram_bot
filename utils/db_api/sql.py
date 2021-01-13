import asyncio
import asyncpg
import logging

from data.config import PG_HOST, PG_PASS, PG_USER

logging.basicConfig(format=u'%(filename)s [LIne:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


async def create_db():
    create_db_command = open("create_db.sql", "r").read()

    logging.info("connecting to db")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST
    )
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table was created")


async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
