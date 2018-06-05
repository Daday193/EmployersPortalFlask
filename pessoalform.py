from flask_wtf import FlaskForm
from wtforms import  StringField,Form,DateField
from wtforms.validators import DataRequired


class pessoalform(FlaskForm):
    InputNome = StringField("InputNome", validators=[DataRequired()])
    InputNaturalidade = StringField("InputNaturalidade", validators=[DataRequired()])
    InputNascimento = DateField("InputNascimento", validators=[DataRequired()])
    InputNumRG = StringField("InputNumRG", validators=[DataRequired()])
    InputEmissaoRG = DateField("InputEmissaoRG", validators=[DataRequired()])
    InputEmissorRG = StringField("InputEmissorRG", validators=[DataRequired()])
    InputNumCNH = StringField("InputNumCNH", validators=[DataRequired()])
    InputEmissaoCNH = DateField("InputEmissaoCNH", validators=[DataRequired()])
    InputEmissorCNH = StringField("InputEmissorCNH", validators=[DataRequired()])
    InputVencimentoCNH = DateField("InputVencimentoCNH", validators=[DataRequired()])
    InputCategoriaCNH = StringField("InputCategoriaCNH", validators=[DataRequired()])
    InputUFCNH = StringField("InputUFCNH", validators=[DataRequired()])
    InputCPF = StringField("InputCPF", validators=[DataRequired()])
    InputPIS = StringField("InputPIS", validators=[DataRequired()])
    InputCasado = StringField("InputCasado", validators=[DataRequired()])
    InputReservista = StringField("InputReservista", validators=[DataRequired()])
    InputCTPS = StringField("InputCTPS", validators=[DataRequired()])
    InputSerieCTPS = StringField("InputSerieCTPS", validators=[DataRequired()])
    InputEmissaoCTPS = DateField("InputEmissaoCTPS", validators=[DataRequired()])
    InputUfCTPS = StringField("InputUfCTPS", validators=[DataRequired()])
