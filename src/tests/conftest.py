import sys
import os
import pytest

from src.services.task_service import TaskService

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

@pytest.fixture(autouse=True)
def reset_task_service():
    service = TaskService()
    service._tasks.clear()  # Limpa o dicionário de tarefas
    yield
    service._tasks.clear()
