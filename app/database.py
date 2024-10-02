import time
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



'''while True:
        
    try:
        conn = psycopg2.connect(host='localhost', dbname='fastapi', user='postgres', password='Florajedan1#', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database conection was succesfull!")

        break 

    except Exception as error:
        print("Connection to database failed")
        print("Error", error)
        time.sleep(2)'''