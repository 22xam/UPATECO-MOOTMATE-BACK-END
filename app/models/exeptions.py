from werkzeug.exceptions import HTTPException
from flask import jsonify

class BadRequest(HTTPException):
    def __init__(self, description="Solicitud incorrecta"):
        super().__init__(description)
        self.status_code = 400

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'descripción': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class InsufficientStorage(HTTPException):
    def __init__(self, description="Espacio de almacenamiento insuficiente"):
        super().__init__(description)
        self.status_code = 507

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'descripción': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class NotModified(HTTPException):
    def __init__(self, description="No Modificado"):
        super().__init__(description)
        self.status_code = 304

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'descripción': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

##from .exeptions import CustomException

class FilmNotFound(CustomException):
    def __init__(self, film_id):
        description = f"Film with id {film_id} not found"
        super().__init__(status_code=404, name="Film Not Found", description=description)

class InvalidDataError(CustomException):
    def __init__(self, description="Invalid Data"):
        super().__init__(status_code=400, name="Invalid Data Error", description=description)   