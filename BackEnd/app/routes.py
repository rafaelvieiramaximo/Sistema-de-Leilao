#Define as "rotas", ou seja, os URLs que sua aplicação vai expor para o usuário, 
# como /produtos, /usuarios, etc.

from flask import Blueprint, jsonify, request
from models.users_model import Usuario
from models.product_model import Produto
from models.auction_model import Lance
from models.payment_model import Pagamento
from models.freight_model import Frete
from models.appraisal_model import Avaliacao
from models.community_model import Comunidade
    
from __init__ import db


routes = Blueprint('/', __name__)

#Blueprint é uma maneira de não precisar atribuir rotas especificas
#para uma aplicação

#Rotas para usuários

@routes.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.objects.all()
    return jsonify([u.to_dict() for u in usuarios]), 201


@routes.route('/usuario/<int:id>', methods=['GET'])
def get_usuarios_id(id):
    usuario = Usuario.objects.get(id)
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

@routes.route('/usuario/<int:id>', methods=['PUT'])
def edit_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.get_json()
        usuario.nome = data.get('nome', usuario.nome)
        usuario.email = data.get('email', usuario.email)
        usuario.senha = data.get('senha', usuario.senha)
        usuario.reputacao = data.get('reputacao', usuario.reputacao)
        db.session.commit()
        return jsonify(usuario.to_dict())
    return jsonify({'message': 'Usuario nao encontrado'}), 404

@routes.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario deletado com sucesso'}), 204
    return jsonify({'message': 'Usuario nao encontrado'}), 404

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

@routes.route('/pagamento', methods=['POST'])
def create_pagamento():
    data = request.get_json()
    new_payment = Pagamento(
        id_usuario=data['id_usuario'],
        id_produto=data['id_produto'],
        valor_total=data['valor_total'],
        forma_pagamento=data['forma_pagamento'],
        status=data['status']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201


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

@routes.route('/lance/<int:id_produto>', methods=['GET'])
def get_lance_pr_id(id_produto):
    lances = Lance.query.filter_by(id_produto=id_produto).all()
    if lances:
        return jsonify([lance.to_dict() for lance in lances])
    return jsonify({'message': 'Lance nao encontrado'}), 404

@routes.route('/lance', methods=['POST'])
def postar_lance():
    data = request.get_json()
    new_lance = Lance(
        valor_lance = data['valor_lance'],
        data_lance = data['data_lance'],
        id_usuario = data['id_usuario'],
        id_produto = data['id_produto']
    )
    db.session.add(new_lance)
    db.session.commit()
    return jsonify(new_lance.to_dict()), 201

#Rotas para avaliações
@routes.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    return jsonify([a.to_dict() for a in avaliacoes])

@routes.route('/avaliacao/<int:id_produto>', methods=['GET'])
def get_avaliacao_pr_id(id_produto):
    avaliacoes = Avaliacao.query.filter_by(id_produto=id_produto).all()
    if avaliacoes:
        return jsonify([avaliacao.to_dict() for avaliacao in avaliacoes])
    return jsonify({'message': 'Avaliacao nao encontrada'}), 404


@routes.route('/avaliacao', methods=['POST'])
def postar_avaliacao():
    data = request.get_json()
    new_avaliacao = Avaliacao(
        texto = data['texto'],
        data = data['data'],
        id_usuario = data['id_usuario'],
        id_produto = data['id_produto']
    )
    db.session.add(new_avaliacao)
    db.session.commit()
    return jsonify(new_avaliacao.to_dict()), 201

