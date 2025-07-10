from fastapi import FastAPI
# from controller.camaras_controller import router as camaras_router

app = FastAPI(title="API de camaras")

@app.get("/")
def read_root():
    return {"mensaje":"API funcionando correctamente"}

# app.include_router(camaras_router, prefix="/camaras")
