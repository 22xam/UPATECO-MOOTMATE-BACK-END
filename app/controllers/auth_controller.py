from ..models.UsuarioModels import UsuarioModel
from flask import request, session, jsonify

class UsuarioController:
    @classmethod
    def login(cls):
        data = request.json
        usuario = UsuarioModel(
            alias = data.get('alias'),
            contrasena = data.get('contrasena')
        )

        if UsuarioModel.is_registered(usuario):
            session['alias'] = data.get('alias')
            return {"message": "Sesion iniciadas"},200
        else:
            return {"message": "Usuario o contraseña incorrectos"},401
    
    @classmethod
    def logout(cls):
        session.pop('alias', None)
        return {"message": "Sesion cerrada"}, 200 
    
    @classmethod
    def crear_usuario(cls):
        data = request.json
        usuario = UsuarioModel(**data)

        # Verificar si el correo ya existe en la base de datos
        if UsuarioModel.correo_existente(usuario):
            # El correo ya existe en la base de datos, devuelve un mensaje de error
            return jsonify({'message': 'El correo ya está registrado'}), 400
        elif not UsuarioModel.alias_disponible(usuario):
            # El alias no está disponible, devuelve un mensaje de error
            return jsonify({'message': 'El alias ya está en uso'}), 400
            # El correo no existe, crea el nuevo usuario
        else:    
            
            id_usuario_creado = UsuarioModel.create(usuario)

            if id_usuario_creado is not None:
                 # Si se creó el usuario exitosamente, devuelve una respuesta con el ID del usuario creado
                return jsonify({'message': 'Usuario creado exitosamente', 'id_usuario': id_usuario_creado}), 201
            else:
                 # En caso de error
                 return jsonify({'message': 'No se pudo crear el usuario'}), 500

        