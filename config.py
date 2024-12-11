# Configurações da aplicação (ex.: banco de dados, chave secreta)


def init_db(app, db):
    
    app.config['SECRET_KEY'] = 'sua_chave_secreta'

    from app.models.brinquedo import Brinquedo
    from app.models.carteira import Carteira
    from app.models.duvida import Duvida
    from app.models.usuario import Usuario
    from app.models.petiscoCachorro import PetiscoCachorro
    from app.models.petiscoGato import PetiscoGato
    with app.app_context():
        # Cria as tabelas no banco de dados
        db.create_all()