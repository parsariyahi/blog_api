from tests.utils.user import create_random_user
from tests.utils.token import verify_jwt_token_sub

def test_generate_token(client, db_session):
    email = "test@some.com"
    password = "test123456"
    user = create_random_user(db_session, email=email, password=password)

    payload = {
        "username": email,
        "password": password,
    }

    response = client.post("/auth/token", data=payload)
    json_response = response.json()

    access_token_sub = email

    access_token = json_response["access_token"]

    assert response.status_code == 200
    assert verify_jwt_token_sub(access_token_sub, access_token) == True