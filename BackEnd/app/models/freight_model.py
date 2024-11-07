from mongoengine import Document, StringField, FloatField, IntField, ReferenceField
#Modulção da Tabela Frete
class Frete(Document):
    cte = IntField(primary_key=True, required=True)
    tipo_frete = StringField(max_length=255, required=True)
    valor_frete = FloatField()
    prazo_entrega = IntField()
    id_pagamento = ReferenceField('Pagamento', required=True)
