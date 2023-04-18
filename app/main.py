from fastapi import FastAPI
from app.router import auth
from app.router import product

app = FastAPI()

# 로그인 관련 라우터
app.include_router(auth.router)

# 상품 관련 라운터
app.include_router(product.router)