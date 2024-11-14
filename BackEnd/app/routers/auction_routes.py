from flask_restful import Resource, reqparse
from app.models.auction_model import Lance_Model
from bson import ObjectId
from flask import jsonify
from mongoengine import DoesNotExist, ValidationError

# Função para serializar ObjectId e renomear campos
def serialize_object_id(data):
    """
    Função para serializar ObjectId para string e lidar com listas ou dicionários,
    renomeando o campo `_id` para `id_lances`.
    """
    if isinstance(data, dict):
        if '_id' in data:
            data['id_lance'] = str(data.pop('_id'))
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

_lance_parser = reqparse.RequestParser()
_lance_parser.add_argument('valor_lance', type=float, required=True, help="Valor do lance é obrigatório")
_lance_parser.add_argument('data_lance', type=str, required=True, help="Data do lance é obrigatório")
_lance_parser.add_argument('id_usuario', type=str, required=True, help="ID do usuário é obrigatório")
_lance_parser.add_argument('id_produto', type=str, required=True, help="ID do produto é obrigatório")

class Lances(Resource):
    def get(self):
        """
        Listar todos os lances.

        Returns:
            json: Lista de lances.
        """
        try:
            lances = Lance_Model.objects.all()
            lances_list = [serialize_object_id(lances.to_mongo().to_dict()) for lances in lances]
            return jsonify(lances_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
class Lance(Resource):
    def get(self, id_lance):
        """
        Obter um lances específico pelo ID.

        Args:
            id_lances (str): O ID do lances.

        Returns:
            json: O lances encontrado ou uma mensagem de erro.
        """
        try:
            lance = Lance_Model.objects.get(id=id_lance)
            lance_data = serialize_object_id(lance.to_mongo().to_dict())
            return lance_data, 200
        except DoesNotExist:
            return {"error": "lances não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500
        
    def post(self):
        """
        Criar um novo lances.

        Returns:
            json: Mensagem de sucesso com o ID do lances criado.
        """
        data = _lance_parser.parse_args()
        # Convertendo os IDs para ObjectId
        data['id_usuario'] = ObjectId(data['id_usuario'])
        data['id_produto'] = ObjectId(data['id_produto'])
        
        try:
            novo_lances = Lance_Model(**data).save()
            return {"message": f"lances {novo_lances.id} criado com sucesso!"}, 201
        except ValidationError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500
