from app.__init__ import app

#Blueprints
from app.routes.home import homeBlueprint
from app.routes.usuario import usuarioBlueprint
from app.routes.adm import admBlueprint
from app.routes.produto import produtoBlueprint

#Registrando minhas Blueprints
def init_app(app):
    app.register_blueprint(homeBlueprint)
    app.register_blueprint(usuarioBlueprint)
    app.register_blueprint(admBlueprint)
    app.register_blueprint(produtoBlueprint)
    
    
