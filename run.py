# Arquivo para rodar o servidor
from flask_login import LoginManager
from app.__init__ import app , db
from app.routes import init_app
from app.models.usuario import Usuario
from config import init_db

init_app(app)
init_db(app, db)

login_manager = LoginManager()
login_manager.login_view = 'usuario.logar'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)