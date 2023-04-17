from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from app.database import SECRET_KEY,ALGORITHM,ACCESS_EXPIRE_MINUTES
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
# from schema import create_response


# JWT 토큰 반환
def get_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encode_jwt

# def decode_token(token: str):
#     try:
#         decode_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
#         return decode_token if decode_token["exp"] >= datetime.time() else None
#     except:
#         return{}

# JWT토큰이 유효한 토큰인지 체크
class JWT_check(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWT_check, self).__init__(auto_error=auto_error)

    # HTTP 헤더에서 토큰값을 추출후 요휴성 판단
    async def __call__(self, request: Request):
        check: HTTPAuthorizationCredentials = await super(JWT_check, self).__call__(request)
        
        if check:
            if not check.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="유효하지 않은 토큰입니다.")
            if not self.verfity_jwt(check.credentials):
                raise HTTPException(
                    status_code=403, detail="유효하지 않은 토큰입니다.")
            return check.credentials
        else:
            raise HTTPException(
                status=403, detail="유효하지 않은 토큰입니다.")

    # JWT토큰의 페이로드를 확인
    def verfity_jwt(Self, jwttoken: str):
        isTokenValid: bool = False
        try:
            payload = jwt.decode(jwttoken, SECRET_KEY, algorithms=[ALGORITHM])
        except:
            payload = None
        
        if payload:
            isTokenValid = True
        return isTokenValid