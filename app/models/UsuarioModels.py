from .entities.Usuario import Usuario
from ..database import DatabaseConnection

class UsuarioModel(Usuario):

    @classmethod
    def get_usuario(cls, usuario):
        try:
            query = "SELECT * FROM usuarios WHERE id_usuario = %s"
            params = (usuario.id_usuario,)
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                usuario = cls(
                    id_usuario=result[0],  # Índice 0 corresponde a id_usuario
                    nombre=result[1],       # Índice 1 corresponde a nombre
                    apellido=result[2],     # Índice 2 corresponde a apellido
                    alias=result[3],        # Índice 3 corresponde a alias
                    correo=result[4],       # Índice 4 corresponde a correo
                    contrasena=result[5],   # Índice 5 corresponde a contrasena
                    id_tipo_estado=result[6],  # Índice 6 corresponde a id_tipo_estado
                    fecha_creacion=result[7]  # Índice 7 corresponde a fecha_creacion
                   )
                return usuario
            # Si no se encuentra el usuario
            return None
        except Exception as e:
           # Captura la excepción y devuelve un diccionario con el código de error y la descripción
            return {"error_code": 500, "error_description": str(e)}
        finally:
            DatabaseConnection.close_connection()
    
    @classmethod
    def is_registered(cls,usuario):
        query = """select id_usuario from usuarios WHERE alias = %(alias)s 
                    and contrasena = %(contrasena)s"""
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query,params=params)

        if result is not None:
            return True
        return False
    
    
    @classmethod
    def create(cls, usuario):
        """Crear un nuevo usuario
        Args:
            - usuario (Usuario): Objeto de usuario
        """
        query = """INSERT INTO mensajeria.usuarios (nombre, apellido, alias, correo, contrasena) 
                   VALUES (%s, %s, %s, %s, %s)"""

        params = usuario.nombre, usuario.apellido, usuario.alias, usuario.correo, usuario.contrasena
        DatabaseConnection.execute_query(query, params=params)
        # Después de la inserción, obtén el id_usuario del registro recién creado
        query = "SELECT LAST_INSERT_ID()"
        result = DatabaseConnection.fetch_one(query)
        if result is not None:
            return result[0]  # devuelve el id_usuario
        else:
            return None
    
    @classmethod
    def correo_existente(cls, usuario):
        """Verificar si un correo electrónico existe en la base de datos.
        Args:
            - correo (str): Correo electrónico a verificar
        Returns:
            - bool: True si el correo existe, False si no existe o si hay un error
        """
        query = "SELECT COUNT(*) FROM usuarios WHERE correo = %s"
        params = (usuario.correo,)

        try:
            result = DatabaseConnection.fetch_one(query, params)

            if result is not None and result[0] > 0 :
                return True
            else:
                return False
        except Exception as e:
            # Manejo de errores: puedes registrar el error o realizar otras acciones según tus necesidades
            print(f"Error al verificar el correo electrónico: {str(e)}")
            return False
    
    @classmethod
    def alias_disponible(cls, usuario):
        """Verificar si un alias está disponible en la base de datos.
         Args:
            - alias (str): Alias a verificar
        Returns:
            - bool: True si el alias está disponible, False si ya está en uso o si hay un error
        """
        query = "SELECT COUNT(*) FROM usuarios WHERE alias = %s"
        params = (usuario.alias,)

        try:
          result = DatabaseConnection.fetch_one(query, params)

          if result is not None and result[0] == 0:
             return True  # El alias está disponible
          else:
             return False  # El alias ya está en uso
        except Exception as e:
             # Manejo de errores: puedes registrar el error o realizar otras acciones según tus necesidades
             print(f"Error al verificar la disponibilidad del alias: {str(e)}")
             return False

    @classmethod
    def update(cls, usuario):
        """Actualizar un usuario
        Args:
            - usuario (Usuario): Objeto de usuario
        """
        allowed_columns = {'nombre', 'apellido', 'alias', 'correo', 'contrasena', 'id_tipo_estado'}
        query_parts = []
        params = []
        for key, value in usuario.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(usuario.id_usuario)

        query = "UPDATE mensajeria.usuarios SET " + ", ".join(query_parts) + " WHERE id_usuario = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls, usuario_id):
        try:
            query = "SELECT COUNT(*) FROM mensajeria.usuarios WHERE id_usuario = %s"
            params = (usuario_id,)
            result = DatabaseConnection.fetch_one(query, params)

            if result and result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            return False

    @classmethod
    def delete(cls, usuario_id):
        """Eliminar un usuario
        Args:
            - usuario_id (int): ID del usuario a eliminar
        """
        query = "DELETE FROM mensajeria.usuarios WHERE id_usuario = %s"
        params = (usuario_id,)
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def get_perfil(cls, usuario):
        try:
            query = "SELECT * FROM usuarios WHERE alias = %(alias)s"
            params = usuario.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                usuario = cls(
                    id_usuario=result[0],  # Índice 0 corresponde a id_usuario
                    nombre=result[1],       # Índice 1 corresponde a nombre
                    apellido=result[2],     # Índice 2 corresponde a apellido
                    alias=result[3],        # Índice 3 corresponde a alias
                    correo=result[4],       # Índice 4 corresponde a correo
                    contrasena=result[5],   # Índice 5 corresponde a contrasena
                    id_tipo_estado=result[6],  # Índice 6 corresponde a id_tipo_estado
                    fecha_creacion=result[7]  # Índice 7 corresponde a fecha_creacion
                   )
                return usuario
            # Si no se encuentra el usuario
            return None
        except Exception as e:
           # Captura la excepción y devuelve un diccionario con el código de error y la descripción
            return {"error_code": 500, "error_description": str(e)}
        finally:
            DatabaseConnection.close_connection()