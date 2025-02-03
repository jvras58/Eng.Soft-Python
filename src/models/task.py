from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import AbstractBaseModel

import enum

class TaskStatus(enum.Enum):
    PENDENTE = "Pendente"
    CONCLUIDA = "Concluída"


class Task(AbstractBaseModel):
    """
    Representa a tabela tarefas no banco de dados.
    """

    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    description: Mapped[str] = mapped_column(name='descricao')
    status: Mapped[enum] = mapped_column(enum.Enum(TaskStatus), default=TaskStatus.PENDENTE, name='status')
