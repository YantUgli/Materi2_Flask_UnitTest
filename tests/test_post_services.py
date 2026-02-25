import pytest
from unittest.mock import MagicMock

from blog.services.post_service import PostService

@pytest.fixture
def service():
    return PostService(post_repository=MagicMock())


@pytest.mark.parametrize(
        "post, expected_exception",
        [
            (
                {
                    "title" : "t",
                    "author" : "Jhon Doe",
                    "content" : "belkahjsdlfja",
                    "category" : "Tech"
                }, ValueError
            ),
            (
                {
                    "title" : "tasdfasdfas",
                    "author" : 6, # error author bukan string
                    "content" : "belkahjsdlfja",
                    "category" : "Tech"
                }, ValueError
            ),
        ]

)

def test_validate_post(service, post, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_post(post)

def test_create_post(service):
    post = {
        "uuid": {
                    "title" : "the title",
                    "author" : "Jhon Doe",
                    "content" : "belkahjsdlfja",
                    "category" : "Tech"
                }
    }

    input_post = {
                    "title" : "the title",
                    "author" : "Jhon Doe",
                    "content" : "belkahjsdlfja",
                    "category" : "Tech"
                }
    
    service.post_repository.save.return_value = post

    result = service.create_post(input_post)

    assert result == post

    service.post_repository.save.assert_called_once_with(input_post)