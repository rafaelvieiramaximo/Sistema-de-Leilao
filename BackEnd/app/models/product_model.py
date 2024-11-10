from mongoengine import Document, StringField, FloatField, IntField, DateField, ReferenceField
from app.models.users_model import Usuario_Model
from app.models.category_model import Categoria_Model

#Modulação da Tabela do Produto
class Produto_Model(Document):
    id_produto = IntField(primary_key=True, required=True)
    nome = StringField(max_length=255, required=True)
    descricao = StringField()
    preco_inicial = FloatField(required=True)
    data_inicial = DateField(required=True)
    id_categoria = ReferenceField(Categoria_Model, required=True)
    id_usuario = ReferenceField(Usuario_Model, required=True)

    meta = {'collection': 'Produtos'}