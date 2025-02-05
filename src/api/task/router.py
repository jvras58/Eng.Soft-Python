from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from src.api.task import schemas
from src.commands import commands
from src.database.database import get_session
from src.queries import queries

router = APIRouter()

db_session_type = Annotated[Session, Depends(get_session)]

@router.get('/get_all_tasks', response_model=list[schemas.TaskOut])
def list_tasks(db: db_session_type):
    """
    Obtém uma lista das tasks do banco de dados.
    """
    query = queries.ListTasksQuery(db)
    return query.execute()

@router.get('/task/{task_id}', response_model=schemas.TaskOut)
def get_task(task_id: int, db: db_session_type):
    """
    Obtém um task do banco de dados pelo Id.
    """
    cmd = commands.GetTaskCommand(task_id, db)
    get_task = cmd.execute()
    if get_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return get_task

@router.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: db_session_type, request: Request):
    """
    Adiciona uma nova task ao banco de dados.
    """
    cmd = commands.CreateTaskCommand(task, db)
    new_task = cmd.execute(request)
    return new_task

@router.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task_status(task_id: int, db: db_session_type):
    """
    Atualiza o status de uma task.
    """
    cmd = commands.UpdateTaskStatusCommand(task_id, db)
    updated_task = cmd.execute()
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return updated_task
