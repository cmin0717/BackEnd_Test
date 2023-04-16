from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User_Model(BaseModel):
    phone_num:str
    password:str

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

class pd_change(BaseModel):
    categorie : str
    price : int
    cost : Optional[int] = None
    pd_name : str
    content : Optional[str] = None
    barcode : Optional[int] = None
    ex_date : datetime
    size : Optional[str] = None

class pd_page(BaseModel):
    user_id: int
    page : int

class pd_search(BaseModel):
    user_id: int
    typing : str

    