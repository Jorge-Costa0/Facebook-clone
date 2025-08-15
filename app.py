from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'liocosta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rede_social.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/register',methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

