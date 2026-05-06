import bcrypt
from models.databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, nombre, apellido, email, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)",
                (nombre, apellido, email, hashed_password.decode('utf-8'))
            )
            conn.commit()
            return True, "Usuario registrado exitosamente"
        except Exception as e:
            print(f"Error: {e}")
            return False, str(e)
        finally:
            conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            return usuario
        return None