from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DB_URL = "mysql://root:4856@localhost:3306/payhere"
engine = create_engine(DB_URL, pool_recycle=900)
sessionlocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    except:
        db.rollback()
        print('error 발생!')
    finally:
        db.close()

# jwt token
SECRET_KEY = 'TestKEY'
ALGORITHM = 'HS256'
ACCESS_EXPIRE_MINUTES = 600
