from src.api.task.schemas import TaskCreate

class TaskFactory:
    @staticmethod
    def create(task_data: TaskCreate) -> TaskCreate:
        description = task_data.description
        if task_data.urgent:
            description = "[URGENTE] " + description
        return TaskCreate(description=description, urgent=task_data.urgent)
