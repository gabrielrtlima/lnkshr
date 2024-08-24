from fastapi import FastAPI
from app.api.endpoints import router as url_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Um serviço de encurtamento de URLs",
)

app.include_router(url_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Bem-vindo ao serviço de encurtamento de URLs"}
