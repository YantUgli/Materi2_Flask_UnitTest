from enum import Enum

class PostCategory(Enum):
    TECH = "Tech"
    BUSINESS = "Business"
    Healt = "Health"


class PostService:
    def __init__(self, post_repository):
        self.post_repository = post_repository

    def validate_post(self, post):
        title = post.get("title")
        content = post.get('content')
        author = post.get('author')
        category = post.get('category')

        if not title or not isinstance(title, str) or len(title) < 5:
            raise ValueError("Post title must be a string and 5 character minimum")
        
        if not content or not isinstance(content, str) or len(content) < 5:
            raise ValueError("Content title must be a string and 5 character minimum")

        if not author or not isinstance(author, str):
            raise ValueError("Post author must be a string")
        
        if category not in [category.value for category in PostCategory]:
            raise ValueError("Post Category should be one of .....")

    def create_post(self, post):
        self.validate_post(post)

        post = self.post_repository.save(post)

        return post
    

    def get_all(self):
        return self.post_repository.get_all()