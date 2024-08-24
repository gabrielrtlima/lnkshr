from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.url import URLCreate, URLResponse, URL as URLSchema
from app.services.url_service import (
    create_short_url,
    get_url_by_short_url,
    update_url_clicks,
)
from app.db.database import get_db

router = APIRouter()


@router.post("/encurtar/", response_model=URLResponse)
def encurtar_url(url_create: URLCreate, db: Session = Depends(get_db)):
    try:
        short_url = create_short_url(db, url_create)
        return URLResponse(short_url=short_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{short_url}", response_model=URLSchema)
def get_url(short_url: str, db: Session = Depends(get_db)):
    db_url = get_url_by_short_url(db, short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    update_url_clicks(db, short_url)  # Atualiza o contador de cliques
    return db_url
