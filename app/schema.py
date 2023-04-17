from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 유저 관련
class User_Model(BaseModel):
    phone_num:str
    password:str

# 상품 정보
class pd_registration(BaseModel):
    pd_id: Optional[int]
    user_id : int
    categorie : str
    price : int
    cost : Optional[int] = None
    pd_name : str
    content : Optional[str] = None
    barcode : Optional[int] = None
    ex_date : datetime
    size : Optional[str] = None

# 상품 수정
class pd_change(BaseModel):
    categorie : str
    price : int
    cost : Optional[int] = None
    pd_name : str
    content : Optional[str] = None
    barcode : Optional[int] = None
    ex_date : datetime
    size : Optional[str] = None

# 페이지 관련
class pd_page(BaseModel):
    user_id: int
    page : int

# 검색 관련
class pd_search(BaseModel):
    user_id: int
    typing : str

# 응답 관련
class meta_data(BaseModel):
    code : int
    msg : str

# 해당 조건에 맞게 응답하는 함수
def create_response(data: any, status_code : int = 200, msg : str = 'OK'):
    meta = meta_data(code= status_code, msg=msg)
    res_data = {'meta':meta.dict(), 'data':data}
    return JSONResponse(content=res_data, status_code=status_code)