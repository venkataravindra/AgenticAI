#create_engine used to create mysql class , this is a factory class used to connect to mysql database
from sqlalchemy import create_engine
#sessionmaker is used to create sessions
#declarative_base - used to create tables
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/emp_db"

#used to connect with database
engine = create_engine(DATABASE_URL)


#used to create session
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#used to create tables using declarative base
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()




