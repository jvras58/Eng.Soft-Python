from src.models.task import Task, TaskStatus

def test_task_como_concluido():
    task = Task(1, "Teste")
    assert task.status == TaskStatus.PENDENTE
    task.mark_task_done()
    assert task.status == TaskStatus.CONCLUIDA
