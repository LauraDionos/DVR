def construir_urls_rtsp(usuario: str, contrasena: str, ip_dvr: str, canales: list[str]) -> dict:
    urls = {}
    for canal in canales:
        urls[canal] = f"rtsp://{usuario}:{contrasena}@{ip_dvr}:554/Streaming/Unicast/channels/{canal}"
    return urls
