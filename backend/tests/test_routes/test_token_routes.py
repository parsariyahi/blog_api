from core.config import settings
from tests.utils.user import create_random_user
from tests.utils.token import verify_jwt_token_sub

def test_generate_token(client, db_session):
    user = create_random_user(db_session, email=settings.TEST_USER_EMAIL, password=settings.TEST_USER_PASSWORD)

    payload = {
        "username": settings.TEST_USER_EMAIL,
        "password": settings.TEST_USER_PASSWORD,
    }

    response = client.post("/auth/token", data=payload)
    json_response = response.json()

    access_token_sub = settings.TEST_USER_EMAIL

    access_token = json_response["access_token"]

    assert response.status_code == 200
    assert verify_jwt_token_sub(access_token_sub, access_token) == True