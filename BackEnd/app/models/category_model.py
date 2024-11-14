from mongoengine import Document, StringField, FloatField, IntField, DateField, ReferenceField

class Categoria_Model(Document):
    nome = StringField(max_length=255, required=True)

    meta = {"collection": "Categoria"}