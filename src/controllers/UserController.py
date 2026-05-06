from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema, UsuarioLogin
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.UsuarioModel = UsuarioModel()

    def register_user(self, nombre, apellido, email, password): 
        try:
            nuevo_usuario = UsuarioSchema(nombre=nombre, apellido=apellido, email=email, password=password)
            success, msg = self.UsuarioModel.registrar(nombre, apellido, email, password)
            return success, msg
        except ValidationError as e:
            return False, e.errors()[0]['msg']
        
    def login(self, email, password):
        try:
            usuario_login = UsuarioLogin(email=email, password=password)
            user = self.UsuarioModel.validar_login(usuario_login.email, usuario_login.password)
            if user:
                return user, "Login exitoso"
            else:
                return None, "Credenciales incorrectas"
        except ValidationError as e:
            return None, e.errors()[0]['msg']