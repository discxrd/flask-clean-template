from flask import render_template

from app_name.example_blueprint import bp


@bp.route('/')
def index():
    return render_template("index.html")
