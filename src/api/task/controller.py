
from sqlalchemy.orm import Session
from api.task import schemas
from src.models import models

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate, description: str):
    db_task = models.Task(description=description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, new_status: models.TaskStatus):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = new_status
        db.commit()
        db.refresh(db_task)
    return db_task
