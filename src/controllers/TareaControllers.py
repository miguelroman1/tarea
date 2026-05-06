from models.TareasModel import TareaModel             

class TareaController:
    def __init__(self):
        self.model = TareaModel()

    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self, id_usuario, titulo, descripcion, prioridad, clasificacion):
        if not titulo:
            return False, "El título es obligatorio"
        
        self.model.crear(id_usuario, titulo, descripcion, prioridad, clasificacion)
        return True, "Tarea creada exitosamente"