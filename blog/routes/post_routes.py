from flask import Blueprint, request
from blog.services.post_service import PostService
from blog.repostory.post_repository import PostRepository

post_blueprint = Blueprint("post_routes", __name__)

post_service = PostService(post_repository=PostRepository())

@post_blueprint.route("/posts", methods=['POST'])
def create_post():
    data = request.get_json()
    try:
        post = post_service.create_post(data)
    except ValueError as e:
        return {'error' :str(e) }, 400
    return post, 201

@post_blueprint.route("/posts/<string:id>", methods=['GET'])
def get_post(id):
    pass

@post_blueprint.route("/posts/<string:id>", methods=['DELETE'])
def delete_post(id):
    pass

@post_blueprint.route("/posts", methods=['GET'])
def get_all():
    posts = post_service.get_all()
    return posts

@post_blueprint.route("/posts/category/<string:category>", methods=['GET'])
def get_posts_by_category():
    pass


