from enum import Enum

class TaskStatus(Enum):
    PENDENTE = "Pendente"
    CONCLUIDA = "Concluída"

class Task:
    def __init__(self, id: int, description: str, status: TaskStatus = TaskStatus.PENDENTE):
        self.id = id
        self.description = description
        self.status = status

    def marcar_como_concluido(self):
        self.status = TaskStatus.CONCLUIDA

    def __repr__(self):
        return f"<Task {self.id}: {self.description} [{self.status.value}]>"
