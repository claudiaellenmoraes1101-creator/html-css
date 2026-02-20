from flask import Blueprint, render_template
from routes import db, Usuario


users_bp = Blueprint('usuario', __name__, template_folder='templates')


@users_bp.route('/usuarios/<nome>')
def listar_usuarios(nome):
    usuarios = Usuario.query.all()
    return {"usuarios": [u.nome for u in usuarios]}