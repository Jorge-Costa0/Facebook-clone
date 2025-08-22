from flask import Blueprint, request, jsonify
from db.database import db
from models.post import Post
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

posts_bp = Blueprint("posts", __name__)

# Criar post
@posts_bp.route("/create", methods=["POST"])
@jwt_required()
def create_post():
    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"error": "Conteúdo não pode ser vazio"}), 400

    user_id = get_jwt_identity()
    new_post = Post(content=content, user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post criado com sucesso", "post_id": new_post.id}), 201


# Listar todos os posts (feed)
@posts_bp.route("/", methods=["GET"])
@jwt_required()
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    output = []
    for post in posts:
        output.append({
            "id": post.id,
            "content": post.content,
            "created_at": post.created_at,
            "user": post.user.username
        })
    return jsonify(output)


# Deletar post (apenas o dono pode)
@posts_bp.route("/<int:post_id>", methods=["DELETE"])
@jwt_required()
def delete_post(post_id):
    user_id = get_jwt_identity()
    post = Post.query.get_or_404(post_id)

    if post.user_id != user_id:
        return jsonify({"error": "Você não pode deletar este post"}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deletado com sucesso"})
