from flask import Flask, request, Blueprint, jsonify
from db.database import db
from models.user import User, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



auth_dp = Blueprint("auth",  __name__)

@auth_dp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not  email or not password:
        return jsonify({"error":"Todos os campos são obrigatorios"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado"}), 400
    

    new_user =  User(username=username, email=email)
    new_user.set_password(password)


    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

@auth_dp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return  jsonify({"error": "credênçias invalidas"}), 401

    token = create_access_token(indentity=User.id)
    return jsonify({"token": token, "username": User.username}), 200
 
@auth_dp.route('/me', methods=['GET'])
@jwt_required()
def me ():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "id": user_id,
        "username": user.username,
        "email": user.email

    }) 
    
