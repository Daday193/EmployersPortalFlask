from flask import  render_template,session
from flask import Flask,redirect,url_for
from forms import Loginform
from pessoalform import pessoalform
from parentescoform import parentescoform
from trabalhoform import trabalhoform
import os.path

import models
import contracheques

app = Flask(__name__)
app.config.from_object(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/login/", methods=["GET","POST"])
def login():
    global form
    form = Loginform()
    nome = str(form.inputEmail.data).upper()
    result = models.conn.execute(models.s, nome=form.inputEmail.data).fetchone()
    if form.validate_on_submit() and nome == result[2] and form.inputPassword.data.strip()== result[3]:
        global session
        session["username"] = result[0]
        print(session["username"])
        fotos()
        print(result[1])
        return redirect(url_for('index'))

    else:
        print(form.errors)
        return render_template('login.html',
                           form=form)


@app.route("/index/")
def index():
    return render_template('SIDENAVIGATION.html')

@app.route("/construcao/")
def construcao():
    return render_template('construcao.html')

@app.route("/contracheque/")
def contracheque():
    if session["username"]:
        comp = "052018"
        file = comp+"/"+session["username"]+".pdf"
        return redirect(url_for('static', filename=file))
    else:
        print('Matricula diferente!')
    return render_template('construcao.html')

@app.route("/fotos/")
def fotos():
    photos = "fotos/"+session["username"]+".jpg"
    try:
        with open('static/'+photos, 'r') as f:
            return redirect(url_for('static', filename=photos))
    except IOError:
        return redirect(url_for('static', filename="fotos/loginvazio.jpg"))

@app.route("/cadastro/")
def cadastro():
    #return render_template('Side_Cadastro.html')
    return render_template('construcao.html')

@app.route("/pessoal/", methods=['GET', 'POST'])
def pessoal():
    form = pessoalform()
    return render_template('pessoal.html',form=form)

@app.route("/parentesco/", methods=['GET', 'POST'])
def parentesco():
    form = parentescoform()
    return render_template('parentesco.html',form=form)

@app.route("/trabalho/", methods=['GET', 'POST'])
def trabalho():
    form = trabalhoform()
    return render_template('trabalho.html',form=form)


app.run(threaded=True,debug=True, use_reloader=True,host='0.0.0.0')