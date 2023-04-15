from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import hashlib, re

from models import User,Product
from database import get_db

app = FastAPI()

class User_Model(BaseModel):
    phone_num:str
    password:str

class Product_Model(BaseModel):
    user_id : int
    categorie : str
    price : int
    cost : int = None
    pd_name : str
    content : str = None
    barcode : int = None
    ex_date : str
    size : str = None

@app.post('/join')
def join(data:User_Model, db: Session = Depends(get_db)):
    data = dict(data)
    id = data['phone_num']
    # 핸드폰 번호 유효성 확인
    if not re.match(r'^010\d{4}\d{4}$', id):
        return {'code':400,'msg':'휴대번호가 유효하지 않습니다.'}
    # 비밀번호 암호화
    password = hashlib.sha256()
    password.update(data['password'].encode('utf-8'))
    
    db.add(User(phone_num = id, password = password.hexdigest()))
    db.commit()

    return {'code':200, 'msg':"success"}