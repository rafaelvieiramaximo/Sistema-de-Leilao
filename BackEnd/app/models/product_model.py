from mongoengine import Document, StringField, FloatField, IntField, DateField, ReferenceField, UUIDField
from app.models.users_model import Usuario_Model
import uuid
    
#Modulação da Tabela do Produto
class Produto_Model(Document):
    nome = StringField(max_length=255, required=True)
    descricao = StringField()
    preco_inicial = FloatField(required=True)
    data_inicial = DateField(required=True)
    id_categoria = StringField(required=True)
    id_usuario = ReferenceField(Usuario_Model, required=True)

    meta = {'collection': 'Produtos'}