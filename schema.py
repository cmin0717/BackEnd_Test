from pydantic import BaseModel

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