#Para banco de dados
from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


#Isso abaixo indica onde está o nosso banco de dados
#db representa o banco de dados
db = SQLAlchemy()


