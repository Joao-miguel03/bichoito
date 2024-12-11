# Arquivo para rodar o servidor
from app.__init__ import app , db
from app.routes import init_app
from config import init_db

init_app(app)
init_db(app, db)

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)