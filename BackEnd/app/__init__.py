from flask import Flask

from flask_restful import Api    
from dotenv import load_dotenv
from flask_cors import CORS
from app.routers.users_routes import Users, User
from app.routers.product_routes import Produto, Produtos
from app.routers.payment_routes import Pagamentos, Pagamento
from app.routers.freight_routes import Fretes, Frete
from app.routers.community_routes import Comunidades, Comunidade
from app.routers.category_routes import Categorias, Categoria
from app.routers.auction_routes import Lances, Lance
from app.routers.appraisal_routes import Avaliacoes, Avaliacao
from app.db import db

import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env


def create_app():
    app = Flask(__name__)

    api = Api(app)  # Configuração do API Restful

    # Configuração do MongoDB usando MongoEngine
    app.config['MONGODB_SETTINGS'] = {
        'host': os.getenv('DB_KEY') 
    }

    db.init_app(app)

    CORS(app)  # Permite CORS para todas as rotas e origens

    # Registro das rotas do aplicativo
    api.add_resource(Users, '/usuarios')
    api.add_resource(User, '/usuario', '/usuario/<string:id_usuario>')
    api.add_resource(Produtos, '/produtos')
    api.add_resource(Produto, '/produto', '/produto/<string:id_produto>')
    api.add_resource(Pagamentos, '/pagamentos')
    api.add_resource(Pagamento, '/pagamento', '/pagamento/<string:id_pagamento>')
    api.add_resource(Fretes, '/fretes')
    api.add_resource(Frete, '/frete', '/frete/<string:cte>')
    api.add_resource(Comunidades, '/comunidades'),
    api.add_resource(Comunidade, '/comunidade', '/comunidade/<string:id_comunidade>')
    api.add_resource(Categorias, '/categorias'),
    api.add_resource(Categoria, '/categoria', '/categoria/<string:id_categoria>')
    api.add_resource(Lances, '/lances')
    api.add_resource(Lance, '/lance', '/lance/<int:id_produto>')
    api.add_resource(Avaliacoes, '/avaliacoes')
    api.add_resource(Avaliacao, '/avaliacao', '/avaliacao/<int:id_produto>')

    #app.register_blueprint(routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)