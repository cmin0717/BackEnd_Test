from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database import Base

# DB 유저 데이터
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_num = Column(String, nullable=False)
    password = Column(String, nullable=False)

# DB 제품 데이터
class product(Base):
    __tablename__ = 'product'
    pd_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    categorie = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    cost = Column(Integer)
    pd_name = Column(String, nullable=False)
    content = Column(Text)
    barcode = Column(Integer)
    ex_date = Column(DateTime, nullable=False)
    size = Column(String)
