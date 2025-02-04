
from src.models.task import TaskStatus

def test_task_como_concluido(task, task_service):
    assert task.status == TaskStatus.PENDENTE
    task_service.mark_task_done(task.id)
    assert task.status == TaskStatus.CONCLUIDA
