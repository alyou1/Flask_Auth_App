from flask import Flask
from .views import views
from .auth import auth
from .models import User, Note
from os import path
from flask_login import LoginManager
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wxcvbnqsdfgh9*'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:airflow97@localhost/tempdb"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app