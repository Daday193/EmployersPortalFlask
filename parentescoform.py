from flask_wtf import FlaskForm
from wtforms import  StringField,Form,DateField
from wtforms.validators import DataRequired


class parentescoform(FlaskForm):
    InputConjuge = StringField("InputConjuge")
    InputFilho1 = StringField("InputFilho1")
    InputFilho1CPF = StringField("InputFilho1CPF")
    InputFilho2 = StringField("InputFilho2")
    InputFilho2CPF = StringField("InputFilho2CPF")
    InputFilho3 = StringField("InputFilho3")
    InputFilho3CPF = StringField("InputFilho3CPF")
    InputFilho4 = StringField("InputFilho4 =")
    InputFilho4CPF = StringField("InputFilho4CPF")
    InputPai = StringField("InputPai", validators=[DataRequired()])
    InputMae = StringField("InputMae", validators=[DataRequired()])