from .tipo_estado_model import TipoEstadoModel
class Usuario:

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.alias = kwargs.get('alias')
        self.correo = kwargs.get('correo')
        self.contrasena = kwargs.get('contrasena')
        self.id_tipo_estado = kwargs.get('id_tipo_estado')
        self.fecha_creacion = kwargs.get('fecha_creacion')

    def serialize(self):

        tipo_estado = TipoEstadoModel.get(TipoEstadoModel(id_tipo_estado = self.id_tipo_estado)).serialize()
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "alias": self.alias,
            "correo": self.correo,
            "contrasena": self.contrasena,
            "id_tipo_estado": self.id_tipo_estado,
            "desripcion": tipo_estado['descripcion'],
            "fecha_creacion": self.fecha_creacion
            
        }