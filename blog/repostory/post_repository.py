import uuid

class PostRepository:
    def __init__(self):
        self.posts = {}

    def save(self, post):
        id = str(uuid.uuid4())
        self.posts[id] = post
        return post
    
    def get_all(self):
        return self.posts