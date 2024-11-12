from flask_restful import Resource, reqparse
from app.models.users_model import Usuario_Model
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from flask import jsonify


# Função para serializar ObjectId
# Função para serializar ObjectId e substituir _id por id_usuario
def serialize_object_id(data):
    if isinstance(data, dict):
        new_data = {key: serialize_object_id(value) for key, value in data.items()}
        # Substituir `_id` por `id_usuario`
        if '_id' in new_data:
            new_data['id_usuario'] = str(new_data.pop('_id'))
        return new_data
    elif isinstance(data, list):
        return [serialize_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data
    

# Parser para os campos de entrada do usuário
_usuario_parser = reqparse.RequestParser()
_usuario_parser.add_argument('nome', 
                             type=str, 
                             required=True, 
                             help="Nome do usuário não pode estar em branco")
_usuario_parser.add_argument('email', 
                             type=str, 
                             required=True, 
                             help="Email do usuário não pode estar em branco")
_usuario_parser.add_argument('senha', 
                             type=str, 
                             required=True, 
                             help="Senha do usuário não pode estar em branco")
_usuario_parser.add_argument('reputacao', 
                             type=float, 
                             required=False, 
                             help="Reputação do usuário")


class Users(Resource):
    """Recurso para operações em múltiplos usuários."""

    def get(self):
        """
        Listar todos os usuários.

        Retorna uma lista de todos os usuários no banco de dados.
        
        Returns:
            json: Lista de usuários.
        """
        usuarios = Usuario_Model.objects.all()  # Consulta no MongoDB
        # Usa o método `to_mongo()` para converter o objeto em um dicionário e depois aplica a função de serialização
        usuarios_list = [serialize_object_id(usuario.to_mongo().to_dict()) for usuario in usuarios]
        return jsonify(usuarios_list)
    
    def delete(self):
        """
        Deletar todos os usuários.

        Remove todos os documentos de usuário do banco de dados.
        
        Returns:
            json: Mensagem de sucesso ou erro.
        """
        try:
            Usuario_Model.objects.delete()  
            return ({"message": "Todos os usuários foram deletados com sucesso"}), 200
        except Exception as e:
            return ({"error": str(e)}), 500  

class User(Resource):
    """Recurso para operações em um usuário específico."""

    def get(self, id_usuario):
        """
        Obter um usuário específico pelo ID.

        Args:
            id_usuario (str): O ID do usuário a ser recuperado.

        Returns:
            json: O usuário encontrado ou uma mensagem de erro.
        """
        try:
            usuario = Usuario_Model.objects.get(id=id_usuario)
            usuario_data = serialize_object_id(usuario.to_mongo().to_dict())  # Aplica a função de serialização
            return (usuario_data), 200
        except DoesNotExist:
            return ({"error": "Usuário não encontrado"}), 404
        except Exception as e:
            return ({"error": str(e)}), 500

    def post(self):
        """
        Criar um novo usuário.

        Cria um usuário com os dados fornecidos no corpo da requisição.
        
        Returns:
            json: Mensagem de sucesso com o ID do usuário criado ou uma mensagem de erro.
        """
        data = _usuario_parser.parse_args()
        try:
            novo_usuario = Usuario_Model(**data).save()  # Não há necessidade de passar id_usuario
            return {"message": "Usuário %s criado com sucesso!" % novo_usuario.id}, 201
        except ValidationError as e:
            return ({"error": str(e)}), 400
        except Exception as e:
            return ({"error": str(e)}), 500


    def put(self, id_usuario):
        """
        Atualizar um usuário existente pelo ID.

        Atualiza os campos do usuário com base nos dados fornecidos.

        Args:
            id_usuario (str): O ID do usuário a ser atualizado.

        Returns:
            json: Mensagem de sucesso ou erro.
        """
        data = _usuario_parser.parse_args()
        try:
            usuario = Usuario_Model.objects.get(id=id_usuario)
            usuario.update(**data)  # Atualiza os campos com os dados fornecidos
            usuario.reload()  # Recarrega o documento atualizado
            return ({"message": "Usuário atualizado com sucesso"}), 200
        except DoesNotExist:
            return ({"error": "Usuário não encontrado"}), 404
        except ValidationError as e:
            return ({"error": str(e)}), 400
        except Exception as e:
            return ({"error": str(e)}), 500

    def delete(self, id_usuario):
        """
        Deletar um usuário específico pelo ID.

        Args:
            id_usuario (str): O ID do usuário a ser deletado.

        Returns:
            json: Mensagem de sucesso ou erro.
        """
        try: 
            usuario = Usuario_Model.objects.get(id=id_usuario)
            usuario.delete()
            return ({"message": "Usuário deletado com sucesso"}), 200
        except DoesNotExist:
            return ({"error": "Usuário não encontrado"}), 404
        except Exception as e:
            return ({"error": str(e)}), 500
