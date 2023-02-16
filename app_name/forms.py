from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ExampleForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
