from flask import Flask
from .routes.error_handlers import errors
from .routes.auth_bp import auth_bp
from flask_cors import CORS

from config import Config


def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(errors)
    app.register_blueprint(auth_bp)
    
    CORS(app, supports_credentials=True)
    
    @app.route('/')
    def index():
        return '<h1>Hola Mundo</h1>'

    
    return app
