from src.models.task import Task, TaskStatus

def test_task_como_concluido():
    task = Task(1, "Teste")
    assert task.status == TaskStatus.PENDENTE
    task.marcar_como_concluido()
    assert task.status == TaskStatus.CONCLUIDA
