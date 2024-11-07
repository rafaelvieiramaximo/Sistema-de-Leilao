from flask_restful import Resource, reqparse
from app.models.users_model import Usuario
from flask import jsonify

class Users(Resource):
    def get(self):
        return jsonify(Usuario.objects())