from flask import Flask
from db.database import db, init_db
from routes import register_routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Carrega configs do config.py
    app.config.from_pyfile("config.py")

    # Inicializa banco
    init_db(app)

    # Registra rotas
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
