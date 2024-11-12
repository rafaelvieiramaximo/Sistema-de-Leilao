from flask_restful import Resource, reqparse
from app.models.product_model import Produto_Model
from app.models.users_model import Usuario_Model
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from flask import jsonify, make_response

def serialize_object_id(data):
    if isinstance(data, dict):
        if '_id' in data:
            data['id_produto'] = str(data.pop('_id'))
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

_produto_parser = reqparse.RequestParser()
_produto_parser.add_argument('nome', type=str, required=True, help="Nome do produto não pode estar em branco")
_produto_parser.add_argument('descricao', type=str, required=True, help="Descrição do produto não pode estar em branco")
_produto_parser.add_argument('preco_inicial', type=float, required=True, help="Preço inicial não pode estar em branco")
_produto_parser.add_argument('data_inicial', type=str, required=True, help="Data inicial não pode estar em branco")
_produto_parser.add_argument('id_usuario', type=str, required=True, help="ID do Usuário não pode estar em branco")
_produto_parser.add_argument('id_categoria', type=str, required=True, help="ID da Categoria não pode estar em branco")

class Produtos(Resource):
    def get(self):
        try:
            produtos = Produto_Model.objects.all()
            produtos_list = [serialize_object_id(produto.to_mongo().to_dict()) for produto in produtos]
            return make_response(jsonify(produtos_list), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

class Produto(Resource):
    def get(self, id_produto):
        try:
            produto = Produto_Model.objects.get(id=id_produto)
            produto_data = serialize_object_id(produto.to_mongo().to_dict())
            return make_response(jsonify(produto_data), 200)
        except DoesNotExist:
            return make_response(jsonify({"error": "Produto não encontrado"}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    def post(self):
        data = _produto_parser.parse_args()
        try:
            usuario = Usuario_Model.objects.get(id=ObjectId(data['id_usuario']))
            if not usuario:
                return make_response(jsonify({"error": "Usuário não encontrado"}), 404)

            novo_produto = Produto_Model(
                nome=data['nome'],
                descricao=data['descricao'],
                preco_inicial=data['preco_inicial'],
                data_inicial=data['data_inicial'],
                id_usuario=usuario,
                id_categoria=data['id_categoria']
            )
            novo_produto.save()
            return make_response(jsonify({"message": f"Produto {str(novo_produto.id)} criado com sucesso!"}), 201)

        except DoesNotExist:
            return make_response(jsonify({"error": "Usuário não encontrado"}), 404)
        except ValidationError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    def put(self, id_produto):
        data = _produto_parser.parse_args()
        try:
            produto = Produto_Model.objects.get(id=id_produto)
            produto.update(
                nome=data['nome'],
                descricao=data['descricao'],
                preco_inicial=data['preco_inicial'],
                data_inicial=data['data_inicial'],
                id_categoria=data['id_categoria']
            )
            return make_response(jsonify({"message": f"Produto {id_produto} atualizado com sucesso!"}), 200)

        except DoesNotExist:
            return make_response(jsonify({"error": "Produto não encontrado"}), 404)
        except ValidationError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    def delete(self, id_produto):
        try:
            produto = Produto_Model.objects.get(id=id_produto)
            produto.delete()
            return make_response(jsonify({"message": f"Produto {id_produto} deletado com sucesso!"}), 200)
        except DoesNotExist:
            return make_response(jsonify({"error": "Produto não encontrado"}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)