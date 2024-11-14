from flask_restful import Resource, reqparse
from app.models.category_model import Categoria_Model
from bson import ObjectId
from flask import jsonify
from mongoengine import DoesNotExist, ValidationError


_categoria_parser = reqparse.RequestParser()
_categoria_parser.add_argument('nome', type=str, required=True, help="nome da Categoria é obrigatório")


def serialize_object_id(data):
    """
    Função para serializar ObjectId para string e lidar com listas ou dicionários,
    renomeando o campo `_id` para `id_pagamento`.
    """
    if isinstance(data, dict):
        if '_id' in data:
            data['id_categoria'] = str(data.pop('_id'))
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

class Categorias(Resource):
     def get(self):
        """
        Listar todos os pagamentos.

        Returns:
            json: Lista de pagamentos.
        """
        try:
            pagamentos = Categoria_Model.objects.all()
            pagamentos_list = [serialize_object_id(pagamento.to_mongo().to_dict()) for pagamento in pagamentos]
            return jsonify(pagamentos_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
class Categoria(Resource):

    def get(self, id_categoria):
        """
        Obter um pagamento específico pelo ID.

        Args:
            id_pagamento (str): O ID do pagamento.

        Returns:
            json: O pagamento encontrado ou uma mensagem de erro.
        """
        try:
            pagamento = Categoria_Model.objects.get(id=id_categoria)
            pagamento_data = serialize_object_id(pagamento.to_mongo().to_dict())
            return pagamento_data, 200
        except DoesNotExist:
            return {"error": "Categoria não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
        
    def post(self):
        """
        Criar um novo pagamento.

        Returns:
            json: Mensagem de sucesso com o ID do pagamento criado.
        """
        data = _categoria_parser.parse_args()
        # Convertendo os IDs para ObjectId
        try:
            novo_pagamento = Categoria_Model(**data).save()
            return {"message": f"Categoria {novo_pagamento.id} criado com sucesso!"}, 201
        except ValidationError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500
        

        


