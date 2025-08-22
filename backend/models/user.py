from db.database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=True)
    email = db.Column(db.String(140), unique=True, nullable=True)
    password_bash = db.Column(db.String(128), nullable=True)

    def set_password(self, password):
        """Gerar hash da senha"""
        self.password_bash = Bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """verifica se a senha está correta"""
        return Bcrypt.check_password_hash(self.password_bash, password)

