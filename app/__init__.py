from flask import Flask
from .routes.error_handlers import errors
from .routes.auth_bp import auth_bp


from config import Config


def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(errors)
    app.register_blueprint(auth_bp)
   
    @app.route('/')
    def index():
        return '<h1>Hola Mundo</h1>'

    
    return app
