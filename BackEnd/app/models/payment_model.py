from mongoengine import Document, StringField, FloatField, IntField, ReferenceField, UUIDField
from app.models.users_model import Usuario_Model
from app.models.product_model import Produto_Model
import uuid
#Modulação da Tabela Pagamentos
class Pagamento_Model(Document):
    id_pagamento = UUIDField(primary_key=True, default=uuid.uuid4)
    usuario = ReferenceField(Usuario_Model, required=True)
    produto = ReferenceField(Produto_Model, required=True)
    valor_total = FloatField(required=True)
    forma_pagamento = StringField(max_length=255, required=True)
    status = StringField(max_length=255, required=True)

    meta = {'collection': 'pagamento'}
