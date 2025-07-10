import cv2
import numpy as np
from repositories.camera_repo import construir_urls_rtsp

class CamarasService:
    def __init__(self, usuario: str, contrasena: str, ip_dvr: str, canales: list[str]):
        self.urls = construir_urls_rtsp(usuario, contrasena, ip_dvr, canales)
        self.capturas = {canal: cv2.VideoCapture(url) for canal, url in self.urls.items()}

    def obtener_grid(self):
        frames = []
        for canal, cap in self.capturas.items():
            ret, frame = cap.read()
            if not ret:
                frame = np.zeros((240, 320, 3), dtype=np.uint8)
                cv2.putText(frame, f"Canal {canal} sin señal", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            else:
                frame = cv2.resize(frame, (320, 240))
            frames.append(frame)

        fila1 = np.hstack(frames[:4])
        fila2 = np.hstack(frames[4:8]) if len(frames) > 4 else np.zeros_like(fila1)
        return np.vstack([fila1, fila2])

    def liberar(self):
        for cap in self.capturas.values():
            cap.release()
        cv2.destroyAllWindows()
