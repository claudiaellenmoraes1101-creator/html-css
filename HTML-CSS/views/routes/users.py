from flask import Blueprint, render_template

users_bp = Blueprint('usuario', __name__, template_folder='templates')

@users_bp.route('/usuario')
def usuario_home():
    return render_template('index.html')

