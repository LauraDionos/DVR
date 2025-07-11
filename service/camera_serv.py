import cv2
import numpy as np

# Credenciales fijas
usuario = "admin"
contrasena = "hil12345"
ip_dvr = "192.168.1.168"

# Construye la URL RTSP para un canal
def url_rtsp(canal: str):
    return f"rtsp://{usuario}:{contrasena}@{ip_dvr}:554/Streaming/Unicast/channels/{canal}"

# Captura una imagen de un canal específico
def captura_frame(canal: str):
    url = url_rtsp(canal)
    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None
    _, jpeg = cv2.imencode(".jpg", frame)
    return jpeg.tobytes()

# Captura y compone una imagen con todas las cámaras en una cuadrícula 2x4
def vista_general():
    canales = ["101", "201", "301", "401", "501", "601", "701", "801"]
    frames = []

    for canal in canales:
        url = url_rtsp(canal)
        cap = cv2.VideoCapture(url)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            frame = np.zeros((240, 320, 3), dtype=np.uint8)
            cv2.putText(frame, f"Canal {canal} sin señal", (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        else:
            frame = cv2.resize(frame, (320, 240))

        frames.append(frame)

    fila1 = np.hstack(frames[:4])
    fila2 = np.hstack(frames[4:8])
    grid = np.vstack([fila1, fila2])

    _, jpeg = cv2.imencode(".jpg", grid)
    return jpeg.tobytes()
