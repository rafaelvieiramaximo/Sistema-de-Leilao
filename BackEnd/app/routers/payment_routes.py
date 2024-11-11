from flask_restful import Resource, reqparse
from app.models.payment_model import Pagamento_Model
from app.models.users_model import Usuario_Model
from app.models.product_model import Produto_Model
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from flask import jsonify
import uuid

# Função para serializar o ObjectId e renomear para `id_pagamento`
def serialize_object_id(data):
    if isinstance(data, dict):
        if '_id' in data:
            data['id_pagamento'] = str(data.pop('_id'))  # Renomeando _id para id_pagamento
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

# Função de parser para dados de pagamento
_pagamento_parser = reqparse.RequestParser()
_pagamento_parser.add_argument('id_usuario', type=str, required=True, help="ID do Usuário não pode estar em branco")
_pagamento_parser.add_argument('id_produto', type=str, required=True, help="ID do Produto não pode estar em branco")
_pagamento_parser.add_argument('valor_total', type=float, required=True, help="Valor total não pode estar em branco")
_pagamento_parser.add_argument('forma_pagamento', type=str, required=True, help="Forma de pagamento não pode estar em branco")
_pagamento_parser.add_argument('status', type=str, required=True, help="Status não pode estar em branco")


class Pagamentos(Resource):
    """Recurso para operações em múltiplos pagamentos."""

    def get(self):
        """
        Listar todos os pagamentos.

        Retorna uma lista de todos os pagamentos no banco de dados.
        """
        try:
            pagamentos = Pagamento.objects.all()
            pagamentos_list = [serialize_object_id(pagamento.to_mongo().to_dict()) for pagamento in pagamentos]
            return jsonify(pagamentos_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500


class Pagamento(Resource):
    """Recurso para Operações em Pagamentos únicos"""

    def get(self, id_pagamento):
        """
        Obter um pagamento pelo ID.
        """
        try:
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)
            pagamento_data = serialize_object_id(pagamento.to_mongo().to_dict())
            return jsonify(pagamento_data)
        except DoesNotExist:
            return jsonify({"error": "Pagamento não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def post(self):
        """
        Criar um novo pagamento.
        """
        data = _pagamento_parser.parse_args()
        try:
            # Verificar se o usuário e o produto existem
            usuario = Usuario_Model.objects.get(id_usuario=data['id_usuario'])
            produto = Produto_Model.objects.get(id_produto=data['id_produto'])

            # Criar o novo pagamento
            novo_pagamento = Pagamento_Model(
                id_pagamento=uuid.uuid4(),
                usuario=usuario,  # Associação com o usuário
                produto=produto,  # Associação com o produto
                valor_total=data['valor_total'],
                forma_pagamento=data['forma_pagamento'],
                status=data['status']
            )
            novo_pagamento.save()

            return jsonify({"message": f"Pagamento {str(novo_pagamento.id_pagamento)} criado com sucesso!"}), 201

        except DoesNotExist:
            return jsonify({"error": "Usuário ou Produto não encontrado"}), 404
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def put(self, id_pagamento):
        """
        Atualizar um pagamento existente pelo ID.
        """
        data = _pagamento_parser.parse_args()
        try:
            # Verificar se o pagamento existe
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)

            # Atualizar os campos do pagamento
            pagamento.update(
                valor_total=data['valor_total'],
                forma_pagamento=data['forma_pagamento'],
                status=data['status']
            )

            return jsonify({"message": f"Pagamento {id_pagamento} atualizado com sucesso!"}), 200

        except DoesNotExist:
            return jsonify({"error": "Pagamento não encontrado"}), 404
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete(self, id_pagamento):
        """
        Deletar um pagamento pelo ID.
        """
        try:
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)
            pagamento.delete()
            return jsonify({"message": f"Pagamento {id_pagamento} deletado com sucesso!"}), 200
        except DoesNotExist:
            return jsonify({"error": "Pagamento não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
