from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DB_USER = 'root'
DB_PASSWORD = '4856'
DB_HOST = "127.0.0.1"
DB_PORT = '3306'
DATABASE = 'payhere'

# DB_URL = "mysql://root:4856@localhost:3306/payhere"
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"
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
