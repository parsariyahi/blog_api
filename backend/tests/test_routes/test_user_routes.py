from core.config import settings

def test_create_user(client):
    data = {
        "email": settings.TEST_USER_EMAIL,
        "password": settings.TEST_USER_PASSWORD,
    }
    response = client.post("/users/add",json=data)

    assert response.status_code == 201
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True