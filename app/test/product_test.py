from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

# JWT 토큰 얻기
def get_token():
    get_token = client.post('/auth/login', json={"phone_num":'01077771111', 'password':'1234'})
    token = get_token.json()['data']['token']
    return f"Bearer {token}"

# 상품 등록 테스트
def test_registration():
    data = {
    'pd_id':1,
    "user_id": 10,
    "categorie": "한식",
    "price": 9000,
    "cost": 3500,
    "pd_name": "불고기 정식",
    "content": "소고기를 이용한 간장 불고기(밥도둑)",
    "barcode": 1149543092,
    "ex_date": "2023-04-17T15:19:54.464Z",
    "size": "big"
    }
    response = client.post('/product/registration', json=data, headers={"Authorization": get_token()})

    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '상품 등록 완료'

# 상품 수정
def test_chage():
    data = {
    "categorie": "한식",
    "price": 10000,
    "cost": 4500,
    "pd_name": "불고기 정식",
    "content": "소고기를 이용한 간장 불고기(밥도둑) - 가격인상",
    "barcode": 1149543092,
    "ex_date": "2023-04-17T15:19:54.464Z",
    "size": "big"
    }
    pd_id = 1
    response = client.put(f'/product/change/{pd_id}', json=data, headers={"Authorization": get_token()})

    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '상품 수정 완료'

# 상품 상세 내역
def test_show():
    pd_id = 1

    response = client.get(f'/product/show/{pd_id}', headers={"Authorization": get_token()})
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == "상품 상세 내역 전송 완료"

# 상품 초성 검색
def test_search():
    data1 = {
        'user_id':10,
        'typing': '불고기'
    }
    data2 = {
        'user_id':10,
        'typing': 'ㅂㄱㄱ'
    }
    data3 = {
        'user_id':10,
        'typing': '제육'
    }

    # like 검색
    response = client.post('product/search', json=data1, headers={"Authorization": get_token()})
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '검색 결과 전송 완료'

    # 초성 검색
    response = client.post('product/search', json=data2, headers={"Authorization": get_token()})
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '검색 결과 전송 완료'

    # 없는 검색
    response = client.post('product/search', json=data3, headers={"Authorization": get_token()})
    assert response.status_code == 401
    assert response.json()['meta']['msg'] == '해당상품은 없습니다.'

# 상품 페이지 검색
def test_page():
    data1 = {
        'user_id':10,
        'page' : 1
    }
    data2 = {
        'user_id':0,
        'page' : 1
    }

    # 해당 페이지에 상품이 존재 할 경우
    response = client.post('/product/page', json=data1, headers={"Authorization": get_token()})
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '해당 페이지 상품 전송 완료'

    # 해당 페이지에 상품이 존재하지 않을 경우
    response = client.post('/product/page', json=data2, headers={"Authorization": get_token()})
    assert response.status_code == 401
    assert response.json()['meta']['msg'] == '해당 페이지에 상품이 존재하지 않습니다.'

# 상품 삭제
def test_delete():
    pd_id = 1

    response = client.delete(f'/product/delete/{pd_id}', headers={"Authorization": get_token()})
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '상품 삭제 완료'

# 테스트 유저 삭제
def test_user_delete():
    user_id = 1
    response = client.delete(f"/auth/delete/{user_id}")
    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '테스트 유저 삭제 완료!'