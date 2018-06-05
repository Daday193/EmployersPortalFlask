from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    inputEmail = StringField("inputEmail", validators=[DataRequired()])
    inputPassword = StringField("inputPassword", validators=[DataRequired()])
    remember_me = BooleanField("remeber_me")

