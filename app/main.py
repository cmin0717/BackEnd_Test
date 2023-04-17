from fastapi import FastAPI
from router import auth
from router import product


app = FastAPI()

# 로그인 관련 라우터
app.include_router(auth.router)

# 상품 관련 라운터
app.include_router(product.router)