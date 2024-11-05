from app import db
from mongoengine import Document, StringField, IntField, ReferenceField, DateField, DateTimeField
#Modulação da tabela Avaliações
class Avaliacao(Document):
    id_avaliacao = IntField(primary_key=True, required=True)
    texto = StringField(required=True)
    data = DateField(required=True)
    usuario = ReferenceField('Usuario', required=True)
    produto = ReferenceField('Produto', required=True)

    meta = {'collection': 'avaliacoes'}
    
