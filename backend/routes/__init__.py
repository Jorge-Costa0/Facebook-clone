from routes.auth import auth_dp
from .auth import auth_dp
from .posts import posts_bp

def register_routes(app):
    app.register_blueprint(auth_dp, url_prefix="/auth")
    app.register_blueprint(posts_bp, url_prefix="/posts")
