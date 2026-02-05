from sqlalchemy import(
    create_engine,URL,MetaData
)

from config import DB_HOST,DB_NAME,DB_PASS,DB_PORT,DB_USER

DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username = DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
) 


metadata_obj = MetaData()

engine = create_engine(DATABASE_URL)


def get_connection():
    return engine.connect()





