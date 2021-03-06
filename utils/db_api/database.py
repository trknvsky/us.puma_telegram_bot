from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URI
import logging

logging.basicConfig(format=u'%(filename)s [LIne:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

db = Gino()


async def create_db():
    logging.info("connecting to db")
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    await db.gino.create_all()





