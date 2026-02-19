#Para banco de dados
from flask import Blueprint

users_bp = Blueprint('usuário', __name__)

@users_bp.route('/usuario')
def usuario():
    return "Página do usuário"