from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

# 회원가입 테스트
def test_join():
    response = client.post('/auth/join', json={'user_id':1,"phone_num":'01077771111', 'password':'1234'})
    assert response.status_code == 200
    assert response.json()['data'] == None

# 로그인 테스트

# 정상적인 로그인
def test_login1():
    response = client.post('/auth/login', json={"phone_num":'01077771111', 'password':'1234'})

    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '로그인 완료!'

# 비밀번호가 틀린 경우
def test_login2():
    response = client.post('/auth/login', json={"phone_num":'01077771111', 'password':'14'})

    assert response.status_code == 401
    assert response.json()['meta']['msg'] == '비밀번호가 일치하지 않습니다.'

# 아이디가 없는 경우
def test_login3():
    response = client.post('/auth/login', json={"phone_num":'0109999999', 'password':'1234'})

    assert response.status_code == 401
    assert response.json()['meta']['msg'] == '입력하신 아이디는 없는 아이디 입니다.'

# 로그아웃 테스트
def test_logout():
    get_token = client.post('/auth/login', json={"phone_num":'01077771111', 'password':'1234'})
    token = get_token.json()['data']['token']

    response = client.get('/auth/logout', headers= {'Authorization': f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()['meta']['msg'] == '로그아웃 완료!'