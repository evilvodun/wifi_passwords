from sqlalchemy import create_engine
from sqlmodel import Session
from typing import Final

CONNECTION_STRING: Final[str] = "sqlite:///database/wifi_database.db"

engine = create_engine(
    CONNECTION_STRING,
    echo=True,
)


def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
