from fastapi import FastAPI
from app.router import auth
from app.router import product
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# 로그인 관련 라우터
app.include_router(auth.router)

# 상품 관련 라운터
app.include_router(product.router)