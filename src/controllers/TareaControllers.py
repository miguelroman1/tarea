from src.models.TareaModel import TareaModel             
from src.models.schemasModel import TareaSchema
from pydantic import ValidationError

class TareaController:
    def __init__(self):
        self.model = TareaModel()

    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva_tarea(self, id_usuario, titulo, des, clas):
        if not titulo:
            return False, "El título es obligatorio"
        
        self.model.crear(id_usuario, titulo, des, clas)
        return True, "Tarea creada exitosamente"
    