import pytest
from app import app
from flask import json
from unittest.mock import MagicMock


from blog.routes import post_routes

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_post(client):
    # Arrange
    post_routes.post_service = MagicMock()
    post = {
        "uuid" : {
            "title" : "the title",
            "author" : "Jhon Doe",
            "content" : "belkahjsdlfja",
            "category" : "Tech"
        }
        }
    
    return_post =  {
        "uuid" : post
        # {
        #     "title" : "the title",
        #     "author" : "Jhon Doe",
        #     "content" : "belkahjsdlfja",
        #     "category" : "Tech"
        # }
        }

    post_routes.post_service.create_post.return_value = return_post
    
    # Action
    response = client.post(
        "/posts", data=json.dumps(post), content_type = "application/json"
    )

    assert response.status_code == 201
    assert return_post == json.loads(response.get_data())