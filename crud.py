from datetime import datetime
from sqlalchemy import Connection,insert,select,delete,update
from models import tasks


def create_task(conn:Connection,title:str,description:str | None=None , due_date:datetime | None=None):
    
    try:
        query = insert(tasks).values(title=title, description=description, due_date=due_date)
        
        print("Tasklar qo'shildi:")
        conn.execute(query)
        conn.commit()
    
    except ValueError as e:
        print(e) 
        conn.rollback()
    
    finally:
        conn.close()
        
def get_task(conn:Connection):
    
    stmt = select(tasks)
    
    rows = conn.execute(stmt)
    
    for row in rows:
        print(row)
        
    conn.commit()
    conn.close()
    
def update_task(
    conn:Connection,
    task_id:int,
    title: str | None=None,
    description: str | None=None,
):
    
    stmt = update(tasks).where(tasks.c.id == task_id).values(title=title,description=description)
    print(f"{task_id}-Update qilindi: ")
    
    print(stmt)
    conn.execute(stmt)
    conn.commit()
    
def delete_task(conn:Connection,task_id:int):
    try:
        stmt = delete(tasks).where(tasks.c.id == task_id)
        print(f"{task_id} task muvafaqiyatli o'chirildi.")
        conn.execute(stmt)
        conn.commit()
        
    except ValueError as e:
        print(e)
        
    finally:
        conn.close()
        
def change_status(conn:Connection,task_id:int):
    try:
        stmt =  select(tasks).where(tasks.c.id == task_id)
        
        rows = conn.execute(stmt)
        
        task = rows.fetchone()
        
        stmt = update(tasks).where(tasks.c.id == task_id).values(completed=not task[3] )
        
        conn.execute(stmt)
        
        conn.commit()
        
    except ValueError as e:
        print(e)
        conn.rollback()
        
        