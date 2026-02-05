from sqlalchemy import(
    Table,Column,String,Integer,Text,DateTime,Boolean
)
from datetime import datetime
from database import metadata_obj

meta = metadata_obj


tasks = Table(
    'tasks',
    meta,
    Column("id",Integer,primary_key=True),
    Column("title",String,nullable=False),
    Column("description",Text),
    Column("completed",Boolean,default=False),
    Column("created_at",DateTime,default=datetime.now()),
    Column("due_date",DateTime,default=datetime.now),
    
    
)