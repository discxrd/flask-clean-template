from flask import render_template

from app_name.example_sub_blueprint import bp


@bp.route('/')
def index():
    return render_template("example_sub_blueprint/index.html")
