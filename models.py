from sqlalchemy.sql import text
from sqlalchemy import create_engine,MetaData
from forms import Loginform
from flask_login import LoginManager,UserMixin, login_required,login_user,current_user


engine = create_engine(
    'mssql+pyodbc://sa:Apcef@123@TMTST'
    )


conn = engine.connect()

s = text("SELECT*FROM TMTST.dbo.LOGIN WHERE Acesso=:nome ")

class User(UserMixin):

    def __init__(self, username, password_hash):
        self.username = form.inputEmail.data
        self.password_hash = form.inputPassword.data


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self): # line 37
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def get_id(self):
        return str(self.id)




#result = conn.execute(s,nome='FILIPE RODRIGUES FERREIRA').fetchone()

#print (result[0],result[1])

