from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from jamo import h2j, j2hcj
from database import get_db
from jwt import JWT_check
import schema
import models


router = APIRouter(prefix='/product')


# 상품 등록
@router.post('/registration', dependencies=[Depends(JWT_check())])
def registration(data:schema.pd_registration, db: Session = Depends(get_db)):
    data = models.product(**dict(data))
    db.add(data)
    db.commit()
    return data

# 상품 부분 수정
@router.put('/change/{pd_id}', dependencies=[Depends(JWT_check())])
def change(pd_id : int, data:schema.pd_change ,db: Session = Depends(get_db)):
    data = dict(data)
    item = db.query(models.product).filter(models.product.pd_id == pd_id).first()
    item.categorie = data['categorie']
    item.price = data['price']
    item.cost = data['cost']
    item.pd_name = data['pd_name']
    item.content = data['content']
    item.barcode = data['barcode']
    item.ex_date = data['ex_date']
    item.size = data['size']
    db.commit()
    return {'msg':'수정완료'}

# 상품 삭제
@router.delete('/delete/{pd_id}', dependencies=[Depends(JWT_check())])
def delete(pd_id : int, db: Session = Depends(get_db)):
    product = db.query(models.product).filter(models.product.pd_id == pd_id).first()
    db.delete(product)
    db.commit()
    return {'msg':'삭제완료'}


# 상품의 리스트보기(페이지 당 10개의 상품)
@router.post('/page', dependencies=[Depends(JWT_check())])
def page(data : schema.pd_page , db: Session = Depends(get_db)):
    data = dict(data)
    user_id = data['user_id']
    page = (data['page'] - 1) * 10
    product = db.query(models.product).filter(models.product.user_id == user_id).offset(page).limit(10).all()
    return product


# 상품의 상세 내역 보기(상세내역??)
@router.get('/show/{pd_id}', dependencies=[Depends(JWT_check())])
def show(pd_id : int, db: Session = Depends(get_db)):
    product = db.query(models.product).filter(models.product.pd_id == pd_id).first()
    return product

# 상품 검색(초성 검색,like 검색)
@router.post('/search', dependencies=[Depends(JWT_check())])
def search(data : schema.pd_search, db: Session = Depends(get_db)):
    data = dict(data)
    user_id = data['user_id']
    typing = data['typing']
    
    search_items = []
    like_item = db.query(models.product).filter(models.product.pd_name.ilike(f"%{typing}%")).filter(models.product.user_id == user_id).all()
    m = [i.pd_name for i in like_item]
    results = db.query(models.product).filter(models.product.pd_name.text(f"name REGEXP '{'[ㄱ-깋]'}'")).all()
    print(results)
    return m

def initial_chcek(words, initial):
    for word in words:
        for x in word:
            temp = h2j(x)
            imf = j2hcj(temp)  # init,middle,final
            print(f"{temp}, {imf}")
    return