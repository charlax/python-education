from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
