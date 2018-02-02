from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

from .settings import EPISODE_COUNT

class EmailForm(FlaskForm):
    email = EmailField('emailInput', validators=[DataRequired(), Email()])
