from flask import Blueprint


bp = Blueprint('example_sub_blueprint', __name__)


from app_name.example_sub_blueprint import routes
