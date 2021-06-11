# Run with python -i to explore

from sqlalchemy import create_engine, Column, String, Integer, select
from sqlalchemy.orm import declarative_base, Session


engine = create_engine("sqlite+pysqlite:///simplest.db", echo=True, future=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))


def main() -> None:
    Base.metadata.create_all(engine)

    user = User(name="Louis")

    with Session(engine) as session:
        session.add(user)
        session.commit()

    with Session(engine) as session:
        user = session.execute(select(User)).scalars().first()
        assert user.name == "Louis"


if __name__ == "__main__":
    main()
