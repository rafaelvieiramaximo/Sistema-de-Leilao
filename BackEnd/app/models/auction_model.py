from __init__ import db
from mongoengine import Document, FloatField, DateField, IntField, ReferenceField
#Modulação da Tabela Lances
class Lance(Document):
    id_lance = IntField(primary_key=True, required=True)
    valor_lance = FloatField(required=True)
    data_lance = DateField(required=True)
    usuario = ReferenceField('Usuario', required=True)
    produto = ReferenceField('Produto', required=True)

    meta = {'collection': 'lances'}