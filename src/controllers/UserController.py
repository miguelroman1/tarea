from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.UsuarioModel = UsuarioModel()

    def register_user(self, nombre, email, password):
        try:
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.UsuarioModel.registrar(nuevo_usuario)
            return success, "Usuario registrado exitosamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']
        
    def login(self, email, password):
        usuario = self.UsuarioModel.validar_login(email, password)

        if usuario:
            return usuario, "Login exitoso"
        else:
            return None, "Correo o contraseña incorrectos"