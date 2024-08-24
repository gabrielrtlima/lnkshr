import string
import random
from fastapi import HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.url import URL
from app.schemas.url import URLCreate, URL as URLSchema
from app.core.config import settings


def create_short_url(db: Session, url_create: URLCreate) -> str:
    for _ in range(10):
        short_url = generate_short_url()
        db_url = URL(original_url=str(url_create.original_url), short_url=short_url)
        db.add(db_url)
        try:
            db.commit()
            return f"{settings.BASE_URL}/{short_url}"
        except IntegrityError:
            db.rollback()
    raise HTTPException(
        status_code=500, detail="Não foi possível gerar uma URL curta única"
    )


def get_url_by_short_url(db: Session, short_url: str) -> Optional[URLSchema]:
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if db_url:
        return URLSchema.from_orm(db_url)
    raise HTTPException(status_code=404, detail="Não foi possível encontrar a URL")


def generate_short_url() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(6))


def get_url_stats(db: Session, short_url: str):
    pass


def update_url_clicks(db: Session, short_url: str):
    pass
