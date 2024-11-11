from flask_restful import Resource
from app.models.payment_model import Pagamento_Model
from bson import ObjectId
from flask import jsonify

def serialize_object_id(data):
    if isinstance(data, dict):
        return {key: serialize_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)  # Converter ObjectId para string
    return data


class Pagamentos(Resource):
    """Recurso para operações em múltiplos pagamentos."""

    def get(self):
        """
        Listar todos os pagamentos.

        Retorna uma lista de todos os pagamentos no banco de dados.

        Returns:
            json: Lista de pagamentos.
        """
        try:
            pagamentos = Pagamento_Model.objects.all()
            pagamentos_list = [serialize_object_id(pagamento.to_mongo().to_dict()) for pagamento in pagamentos]
            return jsonify(pagamentos_list)  # Retorna o JSON corretamente
        except Exception as e:
            return jsonify({"error": str(e)}), 500
