from flask import Blueprint, jsonify
from utils import load_posts, get_post_by_uid

api_blueprint = Blueprint(
    "api",
    __name__,
)


@api_blueprint.route('/api/posts')
def api_posts():
    posts = load_posts()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:pk>')
def api_post(pk):
    posts = get_post_by_uid(pk)
    return jsonify(posts)
