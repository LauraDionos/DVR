from fastapi import APIRouter, Response
from model.camera_config import CameraConfig
from service.camera_serv import CamarasService

router = APIRouter()

@router.post("/ver-camaras/")
def ver_camaras(config: CameraConfig):
    servicio = CamarasService(
        usuario=config.usuario,
        contrasena=config.contrasena,
        ip_dvr=config.ip_dvr,
        canales=config.canales
    )
    grid = servicio.obtener_grid()
    servicio.liberar()

    # Aquí deberías retornar imagen como stream o guardar archivo temporalmente
    return {"mensaje": "Cámaras procesadas correctamente. Backend funcionando."}
