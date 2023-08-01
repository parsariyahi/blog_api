from tests.utils.blog import create_random_blog
from tests.utils.blog import blog_exists
from tests.utils.user import create_random_user
from tests.utils.user import force_authentication


def test_create_a_blog(client, db_session, access_token):
    
    headers= {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    blog = {
        "title": "test blog",
        "content": "this is a test blog",
    }

    response = client.post("/blogs/add", json=blog, headers=headers)
    json_response = response.json()

    assert response.status_code == 201
    assert json_response["title"] == blog["title"]
    assert json_response["content"] == blog["content"]
    assert json_response["slug"] == "test-blog"

def test_fetch_a_blog(client, db_session):
    blog = create_random_blog(db_session)

    response = client.get(f"/blogs/{blog.id}/get")

    assert response.status_code == 200
    assert response.json()["title"] == blog.title

def test_delete_a_blog(client, db_session, access_token, user): 
    blog = create_random_blog(db_session, user)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = client.delete(f"/blogs/{blog.id}/delete", headers=headers) 

    assert response.status_code == 200
    assert blog_exists(db_session, blog) is False