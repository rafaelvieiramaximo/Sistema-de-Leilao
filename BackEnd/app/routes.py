#Define as "rotas", ou seja, os URLs que sua aplicação vai expor para o usuário, 
# como /produtos, /usuarios, etc.

from flask import Blueprint, jsonify, request
from app.models.users_model import Usuario
from app.models.product_model import Produto
from app.models.auction_model import Lance
from app.models.payment_model import Pagamento
from app.models.freight_model import Frete
from app.models.appraisal_model import Avaliacao
from app.models.community_model import Comunidade
    
from app import db


routes = Blueprint('/', __name__)

#Blueprint é uma maneira de não precisar atribuir rotas especificas
#para uma aplicação

#Rotas para usuários

@routes.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

@routes.route('/usuario/<int:id>', methods=['GET'])
def get_usuarios_id(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify(usuario.to_dict())
    return jsonify({'message': 'Usuario nao encontrado'}), 404

@routes.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.get_json()
    new_user = Usuario(
        nome = data['nome'],
        email = data['email'],
        senha = data['senha'],
        reputacao = data['reputacao']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


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
        nome = data['nome'],
        descricao = data['descricao'],
        preco_inicial = data['preco_inicial'],
        data_inicial = data['data_inicial'],
        id_usuario = data['id_usuario']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201 


#Rota para pagamentos
@routes.route('/pagamentos', methods=['GET'])
def get_pagamentos():
    pagamentos = Pagamento.query.all()
    return jsonify([p.to_dict() for p in pagamentos])

#Rotas para fretes
@routes.route('/fretes', methods=['GET'])
def get_fretes():
    fretes = Frete.query.all()
    return jsonify([f.to_dict() for f in fretes])

#Rotas para comunidades
@routes.route('/comunidades', methods=['GET'])
def get_comunidades():
    comunidades = Comunidade.query.all()
    return jsonify([c.to_dict() for c in comunidades])

#Rotas para lances
@routes.route('/lances', methods=['GET'])
def get_lances():
    lances = Lance.query.all()
    return jsonify([l.to_dict() for l in lances])

#Rotas para avaliações
@routes.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    return jsonify([a.to_dict() for a in avaliacoes])


