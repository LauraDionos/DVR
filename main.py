from fastapi import FastAPI
from controller.camera_cont import router

app = FastAPI(title="API de cámaras")
app.include_router(router, prefix="/camaras")
