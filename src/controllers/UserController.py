from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def register_user(self, nombre, email, password):
        try:
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario registrado exitosamente"
        except ValidationError as e:
            return False, e.errosrs()[0]['msg']