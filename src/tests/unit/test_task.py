
from unittest.mock import Mock
from src.api.task.schemas import TaskCreate
from src.models.task import TaskStatus

def test_task_como_concluido(task, task_service):
    assert task.status == TaskStatus.PENDENTE
    task_service.mark_task_done(task.id)
    assert task.status == TaskStatus.CONCLUIDA


# pytest src/tests/unit/test_models.py::test_criar_task
def test_criar_task(task_service):
    """Testa a criação de uma nova tarefa"""
    task_data = TaskCreate(
        description="Nova tarefa"
    )
    
    request = Mock()
    request.client.host = "127.0.0.1"
    
    nova_task = task_service.add_task(task_data, request)
    
    assert nova_task.description == "Nova tarefa"
    assert nova_task.status == TaskStatus.PENDENTE
