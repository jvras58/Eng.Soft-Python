from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

from src.models.base_model import AbstractBaseModel
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
    status: Mapped[TaskStatus] = mapped_column(
        SQLEnum(TaskStatus),
        default=TaskStatus.PENDENTE,
        nullable=False,
        name='status'
    )
