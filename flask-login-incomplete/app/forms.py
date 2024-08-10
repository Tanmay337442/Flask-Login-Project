from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea


forms = Blueprint('forms', __name__)

# ENTER CODE HERE

class UserUpdateForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    update = SubmitField("Save changes")