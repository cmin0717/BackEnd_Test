# Payhere - Test
## 기간 23.04.13 ~ 23.04.18
### git clone
```
git clone https://github.com/cmin0717/BackEnd_Test.git
```
### docker 실행
```
docker-compose up
```
# API
## AUTH
### 회원가입 - "/auth/join" - POST
전화 번호와 비밀번호를 입력 받고 유효성 판단 후 조건에 만족하면 비밀번호 암호화 후 DB저장

### 로그인 - "/auth/login" - POST
위와 같이 전화 번호와 비밀번호를 입력 받는다. 
1. 해당 전화번호가 DB에 있는지 체크
2. DB에 있는 비밀번호와 입력 받은 비밀번호 체크
3. 조건에 모두 만족한다면 JWT토큰과 유저 고유 id를 전달

### 로그아웃 - "/auth/logout" - GET
현재 토큰을 가지고 있는 유저만 요청할수있다.
30초 짜리 토큰을 다시 전달함으로써 로그아웃을 구현하였다.

## PRODUCT
product의 api는 JWT토큰이 없다면 접근하지 못한다.

### 상품 등록 - "/product/registration" - POST
유저 고유 id와 상품 정보를 입력 받는다.
해당 정보를 토대로 DB에 상품 저장

### 상품 부분 수정 - "product/change" - PUT
수정할 product의 고유 아이디와 상품 변경사항과 같이 상품의 다른 정보를 한번에 같이 받아온다.
해당 product 아이디에 해당하는 상품을 가져와 정보를 수정하고 다시 DB에 저장

### 상품 삭제 - "product/delete" - DELETE
삭제할 product의 고유 아이디를 입력받는다.
해당 아이디의 product를 DB에서 삭제

### 상품의 리스트보기 - "product/page" - POST
해당 유저 고유 아이디와 현재 페이지를 입력받는다.
유저의 상품을 다 고른후 페이지에 맞게 offset를 설정하여 현재 페이지에 해당하는 최대 10개의 상품을 전달

### 상품의 상세 내역 보기 - "product/show" - GET
상세 내역을 확인할 product의 고유 아이디를 입력받고 해당 상품의 모든 정보를 전달

### 상품 검색 - "product/search" - POST
상품 검색은 두 가지 형태로 구현하였다.(초성검색, like검색)
해당 유저의 아이디와 현재 타이핑된 문자열을 입력받는다.
1. 먼저 like검색을 실행한다.
2. 해당 유저의 상품명에 타이핑된 값이 있다면 리스트로 관리
3. like 검색 이후 검색된 상품이 1개도 없다면 초성 검색을 실행
4. 모든 검색후 조건에 맞게 전달

## 테스트 코드
작성된 테스트 코드 실행
```
pytest
```
