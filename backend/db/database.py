from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URI"]

    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    
    db.init_app(app)


