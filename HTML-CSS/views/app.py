from flask import Flask
from routes.users import users_bp, usuario_home
from routes.__init__ import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servidor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 
app.register_blueprint(users_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)