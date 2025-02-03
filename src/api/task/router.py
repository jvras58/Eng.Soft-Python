from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.task import schemas
from commands import commands
from database.database import get_session
from queries import queries


router = APIRouter()


db_session_type = Annotated[Session, Depends(get_session)]

@router.get('/get_all_tasks', response_model=list[schemas.TaskOut])
def list_tasks(
):
    """
    Obtém uma lista das tasks do banco de dados.
    """
    query = queries.ListTasksQuery()
    return query.execute()


@router.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: db_session_type ):
    """
    Adiciona uma nova task ao banco de dados.
    """
    cmd = commands.CreateTaskCommand(task)
    new_task = cmd.execute()
    return new_task

@router.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task_status(task_id: int):
    """
    Atualiza o status de uma task.
    """
    cmd = commands.UpdateTaskStatusCommand(task_id)
    updated_task = cmd.execute()
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return updated_task
