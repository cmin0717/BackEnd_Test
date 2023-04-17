from fastapi import APIRouter,Depends
from app.models import User
from app.database import get_db
from app.schema import User_Model, create_response
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.jwt import get_token,JWT_check
from datetime import timedelta
import re


router = APIRouter(prefix='/auth')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# 회원가입
@router.post('/join')
def join(data:User_Model, db: Session = Depends(get_db)):
    data = dict(data)
    id = data['phone_num']
    # 핸드폰 번호 유효성 확인
    if not re.match(r'010\d{4}\d{4}$', id):
        return create_response(None, 400, '유효하지 않은 번호 입니다.')
    # 비밀번호 암호화
    data['password'] = pwd_context.hash(data['password'])

    db.add(User(**data))
    db.commit()

    return create_response(None, 200, '회원 가입에 성공하셨습니다.')

# 로그인(JWT토큰 발급)
@router.post('/login')
def login(data: User_Model , db:Session = Depends(get_db)):
    data = dict(data)
    check = db.query(User).filter(User.phone_num == data['phone_num']).first()

    if not check:
        return create_response(None, 401, '입력하신 아이디는 없는 아이디 입니다.')
    if not pwd_context.verify(data['password'], check.password):
        return create_response(None, 401, '비밀번호가 일치하지 않습니다.')
    
    # 토큰 발급
    token = get_token({'sub':str(check.user_id)})
    result = {'token':token, 'user_id':check.user_id}
    
    return create_response(result, 200, '로그인 완료!')

# 로그아웃(30초짜리 토큰을 반환하면서 토큰을 만료시킨다.)
@router.get('/logout', dependencies=[Depends(JWT_check())])
def logout():
    token = get_token({}, timedelta(seconds=30))
    result = {'token':token}
    return create_response(result, 200, '로그아웃 완료!')

# 유저 삭제(테스트 코드용)
@router.delete('/delete/{user_id}')
def user_delete(user_id : int, db: Session = Depends(get_db)):
    item = db.query(User).filter(User.user_id == user_id).first()
    db.delete(item)
    db.commit()
    return create_response(None, 200, '테스트 유저 삭제 완료!')