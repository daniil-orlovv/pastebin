from datetime import datetime

from pydantic import BaseModel, Field, field_validator

TTL_FORMAT = '%d-%m-%Y %H:%M'


class BlockCreate(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    ttl: datetime

    @field_validator('text')
    @classmethod
    def text_not_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError('Текст не может быть пустым')
        return value

    @field_validator('ttl', mode='before')
    @classmethod
    def parse_ttl(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, TTL_FORMAT)
            except ValueError:
                raise ValueError(
                    'Неверный формат даты, ожидается ДД-ММ-ГГГГ ЧЧ:ММ'
                ) from None
        return value

    @field_validator('ttl')
    @classmethod
    def ttl_in_future(cls, value: datetime) -> datetime:
        if value <= datetime.now():
            raise ValueError('Дата окончания должна быть в будущем')
        return value
