import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base

class Ticket(Base):
    __tablename__="SmartOps Test Project"

    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ticket_id=Column(String(50), nullable=False)
    team=Column(String(50), nullable=False)
    status=Column(String(20), nullable=False)
    priority=Column(String(20), nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), onupdate=func.now())