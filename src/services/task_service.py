from sqlalchemy.orm import Session
from src.api.task.controller import create_task, get_tasks, update_task
from src.services.notification_service import NotificationService
from src.models.task import TaskStatus

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def add_task(self, task_data, request):
        from src.factory.tasks_factory import TaskFactory
        task_data = TaskFactory.create(task_data)
        
        db_task = create_task(self.db, task_data, task_data.description, request)
        NotificationService().notify(f"Tarefa criada: {db_task.description}")
        return db_task

    def list_tasks(self):
        return get_tasks(self.db)

    def mark_task_done(self, task_id: int):
        task = update_task(self.db, task_id, TaskStatus.CONCLUIDA)
        if task:
            NotificationService().notify(f"Tarefa concluída: {task.description}")
        return task
