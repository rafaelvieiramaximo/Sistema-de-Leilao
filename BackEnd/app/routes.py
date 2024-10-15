#Define as "rotas", ou seja, os URLs que sua aplicação vai expor para o usuário, 
# como /produtos, /usuarios, etc.

from flask import Blueprint, jsonify, request
from app.models.product_model import Produto
from app import db


routes = Blueprint('/', __name__)

#Blueprint é uma maneira de não precisar atribuir rotas especificas
#para uma aplicação

#Rotas para Produtos
@routes.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos])


@routes.route('/produto/<int:id>', methods=['GET'])
def get_produtos_id(id):
    produto = Produto.query.get(id)
    if produto:
        return jsonify(produto.to_dict())
    return jsonify({'message': 'Produto nao encontrado'}), 404

@routes.route('/produto', methods=['POST'])
def create_produto():
    data = request.get_json()
    new_product = Produto(
        id_produto = data['id_produto'],
        nome = data['nome'],
        descricao = data['descricao'],
        preco_inicial = data['preco_inicial'],
        data_inicial = data['data_inicial'],
        id_usuario = data['id_usuario']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201 
