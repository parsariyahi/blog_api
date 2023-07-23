from tests.utils.blog import create_random_blog

def test_fetch_a_blog(client, db_session):
    blog = create_random_blog(db_session)

    response = client.get(f"/blogs/{blog.id}/get")

    assert response.status_code == 200
    assert response.json()["title"] == blog.title