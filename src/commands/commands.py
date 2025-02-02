from factory.tasks_factory import TaskFactory
from services.task_service import TaskService

class CreateTaskCommand:
    def __init__(self, description: str, urgent: bool = False):
        self.description = description
        self.urgent = urgent

    def execute(self):
        task = TaskFactory.create_task(self.description, self.urgent)
        TaskService().add_task(task)
        return task

class UpdateTaskStatusCommand:
    def __init__(self, task_id: int):
        self.task_id = task_id

    def execute(self):
        task_service = TaskService()
        task = task_service.get_task(self.task_id)
        if task:
            task.marcar_como_concluído()
            return task
        else:
            raise ValueError("Tarefa não encontrada")
