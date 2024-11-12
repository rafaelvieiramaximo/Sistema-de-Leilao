from flask_restful import Resource, reqparse
from app.models.payment_model import Pagamento_Model
from bson import ObjectId
from flask import jsonify
from mongoengine import DoesNotExist, ValidationError

# Função para serializar ObjectId e renomear campos
def serialize_object_id(data):
    """
    Função para serializar ObjectId para string e lidar com listas ou dicionários,
    renomeando o campo `_id` para `id_pagamento`.
    """
    if isinstance(data, dict):
        if '_id' in data:
            data['id_pagamento'] = str(data.pop('_id'))
        # Serializa `ObjectId` nos campos `id_usuario` e `id_produto`
        if 'id_usuario' in data and isinstance(data['id_usuario'], ObjectId):
            data['id_usuario'] = str(data['id_usuario'])
        if 'id_produto' in data and isinstance(data['id_produto'], ObjectId):
            data['id_produto'] = str(data['id_produto'])
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

# Parser para os campos de entrada do pagamento
_pagamento_parser = reqparse.RequestParser()
_pagamento_parser.add_argument('valor', type=float, required=True, help="Valor do pagamento é obrigatório")
_pagamento_parser.add_argument('metodo', type=str, required=True, help="Método de pagamento é obrigatório")
_pagamento_parser.add_argument('id_usuario', type=str, required=True, help="ID do usuário é obrigatório")
_pagamento_parser.add_argument('id_produto', type=str, required=True, help="ID do produto é obrigatório")
_pagamento_parser.add_argument('status', type=str, required=False, help="Status do pagamento")

class Pagamentos(Resource):
    """Recurso para operações em múltiplos pagamentos."""

    def get(self):
        """
        Listar todos os pagamentos.

        Returns:
            json: Lista de pagamentos.
        """
        try:
            pagamentos = Pagamento_Model.objects.all()
            pagamentos_list = [serialize_object_id(pagamento.to_mongo().to_dict()) for pagamento in pagamentos]
            return jsonify(pagamentos_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def post(self):
        """
        Criar um novo pagamento.

        Returns:
            json: Mensagem de sucesso com o ID do pagamento criado.
        """
        data = _pagamento_parser.parse_args()
        # Convertendo os IDs para ObjectId
        data['id_usuario'] = ObjectId(data['id_usuario'])
        data['id_produto'] = ObjectId(data['id_produto'])
        
        try:
            novo_pagamento = Pagamento_Model(**data).save()
            return {"message": f"Pagamento {novo_pagamento.id} criado com sucesso!"}, 201
        except ValidationError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

class Pagamento(Resource):
    """Recurso para operações em um pagamento específico."""

    def get(self, id_pagamento):
        """
        Obter um pagamento específico pelo ID.

        Args:
            id_pagamento (str): O ID do pagamento.

        Returns:
            json: O pagamento encontrado ou uma mensagem de erro.
        """
        try:
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)
            pagamento_data = serialize_object_id(pagamento.to_mongo().to_dict())
            return pagamento_data, 200
        except DoesNotExist:
            return {"error": "Pagamento não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

    def put(self, id_pagamento):
        """
        Atualizar um pagamento existente pelo ID.

        Args:
            id_pagamento (str): O ID do pagamento.

        Returns:
            json: Mensagem de sucesso ou erro.
        """
        data = _pagamento_parser.parse_args()
        data['id_usuario'] = ObjectId(data['id_usuario'])
        data['id_produto'] = ObjectId(data['id_produto'])
        
        try:
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)
            pagamento.update(**data)
            pagamento.reload()  # Recarregar para obter a versão atualizada
            return {"message": "Pagamento atualizado com sucesso"}, 200
        except DoesNotExist:
            return {"error": "Pagamento não encontrado"}, 404
        except ValidationError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id_pagamento):
        """
        Deletar um pagamento pelo ID.

        Args:
            id_pagamento (str): O ID do pagamento.

        Returns:
            json: Mensagem de sucesso ou erro.
        """
        try:
            pagamento = Pagamento_Model.objects.get(id=id_pagamento)
            pagamento.delete()
            return {"message": "Pagamento deletado com sucesso"}, 200
        except DoesNotExist:
            return {"error": "Pagamento não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
