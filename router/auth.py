from fastapi import APIRouter,Depends
from models import User
from database import get_db
from schema import User_Model
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jwt import generate_token,JWT_check
from datetime import timedelta
import re


router = APIRouter(prefix='/auth')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/join')
def join(data:User_Model, db: Session = Depends(get_db)):
    data = dict(data)
    id = data['phone_num']
    # 핸드폰 번호 유효성 확인
    if not re.match(r'^010\d{4}\d{4}$', id):
        return {'code':400,'msg':'휴대번호가 유효하지 않습니다.'}
    # 비밀번호 암호화
    password = pwd_context.hash(data['password'])

    db.add(User(phone_num = id, password = password))
    db.commit()

    return {'code':200, 'msg':"success"}


@router.post('/login')
def login(data: User_Model , db:Session = Depends(get_db)):
    data = dict(data)
    check = db.query(User).filter(User.phone_num == data['phone_num']).first()

    if not check:
        return {'msg':'id 없음'}
    if not pwd_context.verify(data['password'], check.password):
        return {"msg":'비번 다름'}
    
    # 토큰 발급
    token = generate_token({'sub':str(check.user_id)})
    
    return {'msg':token,"user_id":str(check.user_id)}

@router.get('/logout', dependencies=[Depends(JWT_check())])
def logout():
    token = generate_token({}, timedelta(seconds=60))
    return {'msg':token}

@router.get("/users", dependencies=[Depends(JWT_check())])
async def retrieve_all(db: Session = Depends(get_db)):
    a = db.query(User).all()
    return {'a':a}
