from pydantic import BaseModel

class CameraConfig(BaseModel):
    usuario: str
    contrasena: str
    ip_dvr: str
    canales: list[str]
