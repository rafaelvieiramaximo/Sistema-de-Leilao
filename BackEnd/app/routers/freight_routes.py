from flask_restful import Resource, reqparse
from app.models.freight_model import Frete_Model
from bson import ObjectId
from flask import jsonify
from mongoengine import DoesNotExist, ValidationError


_frete_parser = reqparse.RequestParser()
_frete_parser.add_argument('tipo_frete', type=str, required=True, help="Tipo do Frete é obrigatório")
_frete_parser.add_argument('valor_frete', type=float, required=True, help="Valor do Frete é obrigatório")
_frete_parser.add_argument('prazo_entrega', type=str, required=True, help="Prazo da entrega é obrigatório")
_frete_parser.add_argument('id_pagamento', type=str, required=True, help="ID do produto é obrigatório")


def serialize_object_id(data):
    """
    Função para serializar ObjectId para string e lidar com listas ou dicionários,
    renomeando o campo `_id` para `id_pagamento`.
    """
    if isinstance(data, dict):
        if '_id' in data:
            data['cte'] = str(data.pop('_id'))
        # Serializa `ObjectId` nos campos `id_usuario` e `id_produto`
        if 'id_produto' in data and isinstance(data['id_produto'], ObjectId):
            data['id_produto'] = str(data['id_produto'])
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

class Fretes(Resource):
     def get(self):
        """
        Listar todos os pagamentos.

        Returns:
            json: Lista de pagamentos.
        """
        try:
            pagamentos = Frete_Model.objects.all()
            pagamentos_list = [serialize_object_id(pagamento.to_mongo().to_dict()) for pagamento in pagamentos]
            return jsonify(pagamentos_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
class Frete(Resource):

    def get(self, cte):
        """
        Obter um pagamento específico pelo ID.

        Args:
            id_pagamento (str): O ID do pagamento.

        Returns:
            json: O pagamento encontrado ou uma mensagem de erro.
        """
        try:
            pagamento = Frete_Model.objects.get(id=cte)
            pagamento_data = serialize_object_id(pagamento.to_mongo().to_dict())
            return pagamento_data, 200
        except DoesNotExist:
            return {"error": "Frete não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
        
    def post(self):
        """
        Criar um novo pagamento.

        Returns:
            json: Mensagem de sucesso com o ID do pagamento criado.
        """
        data = _frete_parser.parse_args()
        # Convertendo os IDs para ObjectId
        data['id_pagamento'] = ObjectId(data['id_pagamento'])
       
        try:
            novo_pagamento = Frete_Model(**data).save()
            return {"message": f"Frete {novo_pagamento.id} criado com sucesso!"}, 201
        except ValidationError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500
        

        


