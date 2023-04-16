from fastapi import FastAPI
from router import auth
from router import product


app = FastAPI()

app.include_router(auth.router)
app.include_router(product.router)