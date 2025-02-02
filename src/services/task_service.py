class TaskService:
    _instance = None
    _tasks = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskService, cls).__new__(cls)
        return cls._instance

    def add_task(self, task):
        self._tasks[task.id] = task
        from src.services.notification_service import NotificationService
        NotificationService().notify(f"Tarefa criada: {task.description}")

    def get_task(self, task_id):
        return self._tasks.get(task_id)

    def list_tasks(self):
        return list(self._tasks.values())
