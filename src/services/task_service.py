
from api.task.controller import create_task, get_tasks, update_task
from database.database import get_session
from services.notification_service import NotificationService

class TaskService:
    def __init__(self):
        self.db = get_session()

    def add_task(self, task_data):
        from factory.tasks_factory import TaskFactory
        task_data = TaskFactory.create(task_data)
        db_task = create_task(self.db, task_data, task_data.description)
        NotificationService().notify(f"Tarefa criada: {db_task.description}")
        return db_task

    def list_tasks(self):
        return get_tasks(self.db)

    def mark_task_done(self, task_id: int):
        task = update_task(self.db, task_id, "CONCLUIDA")
        if task:
            NotificationService().notify(f"Tarefa concluída: {task.description}")
        return task
