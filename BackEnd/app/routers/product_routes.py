from flask_restful import Resource, reqparse
from app.models.product_model import Produto
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from flask import jsonify

def serialize_object_id(data):
    if isinstance(data, dict):
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

""""Função para campos de entrada de produto"""
_produto_parser = reqparse.RequestParser()
_produto_parser.add_argument('id_produto',
                              type=int,
                              required=True,
                              help="ID do produto não pode estar em branco")
_produto_parser.add_argument('nome',
                              type=str, 
                              required=True,
                              help="Nome do produto não pode estar em branco")
_produto_parser.add_argument('descricao',
                             type=str,
                             required=True, 
                             help="Descricao do produto não pode estar em branco")
_produto_parser.add_argument('preco_inicial', 
                             type=float, 
                             required=True, 
                             help="Preço inicial não pode estar em branco")
_produto_parser.add_argument('data_inicial', 
                             type=str,
                             required=True, 
                             help="Data inicial não pode estar em branco")
_produto_parser.add_argument('id_usuario', 
                             type=str,
                             required=True, 
                             help="Id do Usuário não pode estar em branco")



class Produtos(Resource): 
    """Recurso para operações em múltiplos produtos."""

    def get(self):
        """

        Listar todos os produtos.

        Retorna uma lista de todos os produtos no banco de dados.

        Returns:
            json: Lista de produtos.
        """
        produtos = Produtos.objects.all()
        produtos_list = [serialize_object_id(produto.to_mongo().to_dict()) for produto in produtos]
        return jsonify(produtos_list)
    
class Produto(Resource):
    """Recurso para Operações em Produtos únicos"""

    def get(self, id_produto):

        try:
            produto = Produto.objects.get(id=id_produto)
            produto_data = (serialize_object_id(produto.to_mongo().to_dict()))
            return jsonify(produto_data)
        except DoesNotExist:
            return jsonify({"error": "Produto não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def post(self):
        data = _produto_parser.parse_args()
        try:
            novo_produto = Produto(**data).save()
            return ({"message": "Produto %s criado com sucesso!" % novo_produto.id}), 201
        except ValidationError as e:
            return ({"error": str(e)}), 400
        except Exception as e:
            return ({"error": str(e)}), 500