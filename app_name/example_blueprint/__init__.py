from flask import Blueprint


bp = Blueprint('example_blueprint', __name__)


from app_name.example_blueprint import routes
