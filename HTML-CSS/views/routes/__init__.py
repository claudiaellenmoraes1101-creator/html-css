#Para banco de dados
from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Isso abaixo indica onde está o nosso banco de dados
#db representa o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///servidor.db"
db = SQLAlchemy()
#Aqui estamos conectando nosso banco de dados com a nossa aplicação
db.init_app(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    #primary key é usado para que cada registro tenha uma identificação
    nome = db.Column(db.String(40), nullable=False, unique=True)
    #unique indica que não pode ter registros com os mesmos nomes

