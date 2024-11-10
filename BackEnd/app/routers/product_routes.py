from flask_restful import Resource, reqparse
from app.models.product_model import Produto_Model
from app.models.users_model import Usuario_Model
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
_produto_parser.add_argument('id_categoria', 
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
        produtos = Produto_Model.objects.all()
        produtos_list = [serialize_object_id(produto.to_mongo().to_dict()) for produto in produtos]
        return jsonify(produtos_list)
    
class Produto(Resource):
    """Recurso para Operações em Produtos únicos"""

    def get(self, id_produto):

        try:
            produto = Produto_Model.objects.get(id=id_produto)
            produto_data = (serialize_object_id(produto.to_mongo().to_dict()))
            return jsonify(produto_data)
        except DoesNotExist:
            return jsonify({"error": "Produto não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def post(self):
        data = _produto_parser.parse_args()
        try:
            # Verificar se o usuário existe
            usuario = Usuario_Model.objects.get(id_usuario=data['id_usuario'])
            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 404

            # Criar o novo produto associado ao usuário
            novo_produto = Produto_Model(
                id_produto=data['id_produto'],
                nome=data['nome'],
                descricao=data['descricao'],
                preco_inicial=data['preco_inicial'],
                data_inicial=data['data_inicial'],
                id_usuario=usuario  # Associação com o usuário
            )
            novo_produto.save()

            return jsonify({"message": f"Produto {novo_produto.id_produto} criado com sucesso!"}), 201

        except DoesNotExist:
            return jsonify({"error": "Usuário não encontrado"}), 404
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500