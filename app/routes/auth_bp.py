from flask import Blueprint

from ..controllers.auth_controller import UsuarioController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UsuarioController.login)
auth_bp.route('/logout', methods=['GET'])(UsuarioController.logout)
auth_bp.route('/register', methods=['POST'])(UsuarioController.crear_usuario)
auth_bp.route('/get_user/<int:id_usuario>', methods=['GET'])(UsuarioController.get_user)
auth_bp.route('/profile', methods=['GET'])(UsuarioController.perfil)