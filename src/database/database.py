from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.config import Config


config = Config()
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

def get_session():
    with Session(engine) as session:
        yield session
