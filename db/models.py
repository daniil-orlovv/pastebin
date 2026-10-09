from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy.types import String
from sqlalchemy import UUID

from db.base import Base


class Block(Base):
    __tablename__ = 'blocks'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    short_uuid = Column(String)
    object_name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    ttl = Column(DateTime)

