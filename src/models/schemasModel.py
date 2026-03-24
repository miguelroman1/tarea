from pydantic import BaseModel, Emailstr, Field
from typing import Optional
from datetime import date, time

class UsuarioSchema(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    email: Emailstr
    password: str = Field(..., min_length=8)
    
class TareaSchema(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificaion: str = "personal"