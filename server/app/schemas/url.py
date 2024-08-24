from pydantic import BaseModel, HttpUrl


class URLBase(BaseModel):
    original_url: HttpUrl


class URLCreate(URLBase):
    pass


class URLResponse(BaseModel):
    short_url: str


class URL(URLBase):
    id: int
    short_url: str

    class Config:
        from_attributes = True  # Substitui orm_mode = True
