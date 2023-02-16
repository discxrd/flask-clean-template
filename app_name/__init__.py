from flask import Flask

from config import Config

from app_name.extensions import (
    db, 
    migrate, 
    bcrypt
)

from app_name.example_blueprint import bp as example_bp
from app_name.example_sub_blueprint import bp as example_sub_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Иницилация дополнений к фласку
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Регистрация блюпринтов
    app.register_blueprint(example_bp)
    app.register_blueprint(example_sub_bp, url_prefix="/example_sub_blueprint")

    return app
