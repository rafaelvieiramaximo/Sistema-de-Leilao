from mongoengine import Document, StringField, FloatField, IntField, ReferenceField, DateField
from app.models.payment_model import Pagamento_Model
#Modulção da Tabela Frete

class Frete_Model(Document):
    tipo_frete = StringField(max_length=255, required=True)
    valor_frete = FloatField()
    prazo_entrega = DateField()
    id_pagamento = ReferenceField(Pagamento_Model, required=True)

    meta = {'collections': 'Frete'}