from src.models.task import Task, TaskStatus

class TaskFactory:
    task_id = 1 

    @classmethod
    def create_task(cls, description: str, urgent: bool = False) -> Task:
        task = Task(id=cls.task_id, description=description)
        if urgent:
            task.description = "[URGENTE] " + task.description
        cls.task_id += 1
        return task
