import pytest
from sqlalchemy import Engine, create_engine, event
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from src.models.task import Task, TaskStatus
from src.models.base_model import Base
from src.database.database import get_session
from sqlalchemy.pool import StaticPool
from src.main import app


from src.services.task_service import TaskService

@pytest.fixture
def client(session):
    """
    Contexto de webclient para teste de APIRest

    Returns:
        TestClient: Uma instancia de TestClient do FastAPI.
    """

    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()

    return TestClient(app)


@pytest.fixture
def session():
    """
    Contexto de Session para teste de estrutura de banco de dados.

    Yields:
        Session: Uma instancia de Session do SQLAlchemy
    """
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
        # echo=True,
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.

    Args:
        dbapi_connection: O objeto de conexão com o banco de dados.
        connection_record: O objeto de registro de conexão.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

@pytest.fixture
def task_service(session):
    service = TaskService(session)
    yield service

@pytest.fixture
def task(session):
    """
    Cria uma ingessão de task para os testes.

    Args:
        session (Session): Uma instância de Session do SQLAlchemy.

    Returns:
        Task: Uma instância de task do sistema.
    """
    task = Task(
        description='Teste',
        status=TaskStatus.PENDENTE,
        audit_user_ip='0.0.0.0',
        audit_user_login='tester',
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
