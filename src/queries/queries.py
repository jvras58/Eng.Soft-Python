from services.task_service import TaskService

class ListTasksQuery:
    def __init__(self, db):
        self.db = db

    def execute(self):
        return TaskService(self.db).list_tasks()
