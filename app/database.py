import mysql.connector
from config import Config

class DatabaseConnection:
    _connection = None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host=Config.host,
                user=Config.user,
                port = Config.port,
                password = Config.password,
                database=Config.database
            )
        return cls._connection
    
    @classmethod
    def execute_query(cls, query,params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchone()
    
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchall()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
            
    @classmethod
    def execute_callproc(cls, procedure_name, params=None):
        cursor = cls.get_connection().cursor()
        try:
            cursor.callproc(procedure_name, params)
            cls._connection.commit()
            return cursor
        except mysql.connector.Error as err:
            # Manejar errores de MySQL aquí
            print(f"Error ejecutando el procedimiento almacenado: {err}")
        finally:
            cursor.close()