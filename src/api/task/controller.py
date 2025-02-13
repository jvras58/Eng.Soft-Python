from sqlalchemy.orm import Session
from src.api.task import schemas
from src.models.task import Task, TaskStatus

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate, description: str, request):
    db_task = Task(description=description)
    db_task.audit_user_ip = request.client.host
    db_task.audit_user_login = "admin"
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, new_status: TaskStatus):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = new_status
        db.commit()
        db.refresh(db_task)
    return db_task
