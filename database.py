# A lot of code is from https://docs.sqlalchemy.org/en/13/orm/tutorial.html

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    discord_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

    def __repr__(self):
        return f"<User({self.discord_id}, {self.name})>"


def get_session():
    engine = create_engine('sqlite:///komida.db', echo=True)
    Base.metadata.create_all(engine)

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    return session