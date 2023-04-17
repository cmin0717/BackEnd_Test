from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from jamo import h2j, j2hcj
from app.database import get_db
from app.jwt import JWT_check
from app.schema import *
from app.models import *


router = APIRouter(prefix='/product')


# 상품 등록
@router.post('/registration', dependencies=[Depends(JWT_check())])
def registration(data:pd_registration, db: Session = Depends(get_db)):
    data = product(**dict(data))
    db.add(data)
    db.commit()
    return create_response(None, 200, '상품 등록 완료')



# 상품 부분 수정
@router.put('/change/{pd_id}', dependencies=[Depends(JWT_check())])
def change(pd_id : int, data:pd_change ,db: Session = Depends(get_db)):
    item = db.query(product).filter(product.pd_id == pd_id).first()
    item.categorie = data.categorie
    item.price = data.price
    item.cost = data.cost
    item.pd_name = data.pd_name
    item.content = data.content
    item.barcode = data.barcode
    item.ex_date = data.ex_date
    item.size = data.size
    db.commit()
    return create_response(None, 200, '상품 수정 완료')



# 상품 삭제
@router.delete('/delete/{pd_id}', dependencies=[Depends(JWT_check())])
def delete(pd_id : int, db: Session = Depends(get_db)):
    item = db.query(product).filter(product.pd_id == pd_id).first()
    db.delete(item)
    db.commit()
    return create_response(None, 200, '상품 삭제 완료')



# 상품의 리스트보기(페이지 당 10개의 상품)
@router.post('/page', dependencies=[Depends(JWT_check())])
def page(data : pd_page , db: Session = Depends(get_db)):
    user_id = data.user_id
    page = (data.page - 1) * 10
    item = db.query(product).filter(product.user_id == user_id).offset(page).limit(10).all()
    if len(item) == 0:
        return create_response(None, 401, '해당 페이지에 상품이 존재하지 않습니다.')
    result = {"product":jsonable_encoder(item)}
    return create_response(result, 200, "해당 페이지 상품 전송 완료")



# 상품의 상세 내역 보기(상세내역??)
@router.get('/show/{pd_id}', dependencies=[Depends(JWT_check())])
def show(pd_id : int, db: Session = Depends(get_db)):
    item = db.query(product).filter(product.pd_id == pd_id).first()
    result = {"product":jsonable_encoder(item)}
    return create_response(result, 200, "상품 상세 내역 전송 완료")



# 상품 검색(초성 검색,like 검색)
@router.post('/search', dependencies=[Depends(JWT_check())])
def search(data : pd_search, db: Session = Depends(get_db)):
    user_id = data.user_id
    typing = data.typing
    search_items = []

    like_item = db.query(product).filter(product.pd_name.ilike(f"%{typing}%")).filter(product.user_id == user_id).all()
    words = db.query(product).filter(product.user_id == user_id).all()
    words = [i.pd_name for i in words]
    search_items = [i.pd_name for i in like_item]

    if len(search_items) == 0 :
        search_items = initial_chcek(words,typing)
    if len(search_items) == 0:
        return create_response(None, 401, '해당상품은 없습니다.')
    result = {"search":search_items}
    return create_response(result, 200, '검색 결과 전송 완료')



# 초성 검색 함수
def initial_chcek(words, initial):
    result = []
    for word in words:
        m = []
        for x in word:
            temp = h2j(x)
            imf = j2hcj(temp) 
            m.append(imf[0])
        if initial in ''.join(m):
            result.append(word)
    return result