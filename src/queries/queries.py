from services.task_service import TaskService

class ListTasksQuery:
    def execute(self):
        return TaskService().list_tasks()
