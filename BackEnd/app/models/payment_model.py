from mongoengine import Document, StringField, FloatField, IntField, ReferenceField

#Modulação da Tabela Pagamentos
class Pagamento(Document):
    id_pagamento = IntField(primary_key=True, required=True)
    usuario = ReferenceField('Usuario', required=True)
    produto = ReferenceField('Produto', required=True)
    valor_total = FloatField(required=True)
    forma_pagamento = StringField(max_length=255, required=True)
    status = StringField(max_length=255, required=True)

    meta = {'collection': 'pagamento'}
