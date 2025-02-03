from src.api.task.schemas import TaskCreate
from src.services.task_service import TaskService

class CreateTaskCommand:
    def __init__(self, task_data: TaskCreate, db):
        self.task_data = task_data
        self.db = db

    def execute(self, request):
        return TaskService(self.db).add_task(self.task_data, request)

class UpdateTaskStatusCommand:
    def __init__(self, task_id: int, db):
        self.task_id = task_id
        self.db = db

    def execute(self):
        return TaskService(self.db).mark_task_done(self.task_id)
