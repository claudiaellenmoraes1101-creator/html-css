from routes import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    #primary key é usado para que cada registro tenha uma identificação
    nome = db.Column(db.String(40), nullable=False, unique=True)
    #unique indica que não pode ter registros com os mesmos nomes
