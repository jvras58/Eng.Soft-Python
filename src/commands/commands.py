from api.task.schemas import TaskCreate
from services.task_service import TaskService


class CreateTaskCommand:
    def __init__(self, task_data: TaskCreate):
        self.task_data = task_data

    def execute(self):
        return TaskService().add_task(self.task_data)

class UpdateTaskStatusCommand:
    def __init__(self, task_id: int):
        self.task_id = task_id

    def execute(self):
        return TaskService().mark_task_done(self.task_id)
