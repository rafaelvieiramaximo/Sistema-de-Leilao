#Aqui você inicia o Flask e define configurações básicas, como o banco de dados.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os



load_dotenv()  # Carrega variáveis de ambiente do.env


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)


    #Troca a url do BD pela variavel DB_KEY se utilizando as bibliotecas os e env.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_KEY')  # Caminho do banco de dados

    db.init_app(app)

     # Importa os models para garantir que o SQLAlchemy os reconheça
    from app.models.users_model import Usuario
    from app.models.product_model import Produto
    from app.models.auction_model import Lance
    from app.models.payment_model import Pagamento
    from app.models.freight_model import Frete
    from app.models.appraisal_model import Avaliacao
    from app.models.community_model import Comunidade
    
    # Cria todas as tabelas, respeitando a ordem de dependências
    with app.app_context():
        db.create_all()

    from .routes import routes as routes_bp
    app.register_blueprint(routes_bp)  # Registra as rotas definidas no arquivo routes.py

    return app
