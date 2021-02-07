from sqlalchemy import (Column, Integer, BigInteger, String, Sequence)
from sqlalchemy import sql
from .database import db


class User(db.Model):
    __tablename__='users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    username = Column(String(50))
    full_name = Column(String(100))
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', username='{}', fullname='{}')>".format(self.id, self.username, self.full_name)