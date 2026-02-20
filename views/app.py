from flask import Flask
from routes import db
from routes.users import users_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servidor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Aqui estamos conectando nosso banco de dados com a nossa aplicação
db.init_app(app)

app.register_blueprint(users_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # cria as tabelas
    app.run(debug=True)