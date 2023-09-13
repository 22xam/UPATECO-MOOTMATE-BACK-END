from ...database import DatabaseConnection

class TipoEstadoModel:

    def __init__(self, **kwargs):
        self.id_tipo_estado = kwargs.get('id_tipo_estado')
        self.descripcion = kwargs.get('descripcion')

    def serialize(self):
        return {
            "id_tipo_estado": self.id_tipo_estado,
            "descripcion": self.descripcion,
        }

    @classmethod
    def get(cls, tipo_estado):
        query = """SELECT * FROM mensajeria.tipo_estado 
        WHERE id_tipo_estado = %(id_tipo_estado)s"""
        params = tipo_estado.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_tipo_estado = result[0],
                descripcion = result[1]
            )
        return None
