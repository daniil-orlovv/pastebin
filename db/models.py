from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, Integer
from sqlalchemy.types import String

from db.base import Base


class Block(Base):
    __tablename__ = 'blocks'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    short_uuid = Column(String)
    object_name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    ttl = Column(DateTime)
    views = Column(Integer, nullable=False, default=0, server_default='0')


