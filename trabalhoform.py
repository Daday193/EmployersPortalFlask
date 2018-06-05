from flask_wtf import FlaskForm
from wtforms import  StringField,Form,DateField
from wtforms.validators import DataRequired


class trabalhoform(FlaskForm):
    InputDe = StringField("InputDe", validators=[DataRequired()])
    InputAte = StringField("InputAte", validators=[DataRequired()])
