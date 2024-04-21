from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class ServiceModel(Base):
    __tablename__ = 'service'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    cost =  Column(Float(), nullable=False)
    taxes =  Column(Float(), nullable=False)
    address = Column(String(), nullable=False)
    details = Column(String(), nullable=False)
    createdAt = Column(DateTime(), default=datetime.now(timezone.utc) )
    updateAt = Column(DateTime(), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc) )
    sportmen = relationship("Sportmen")

class Sportmen(Base):
    __tablename__ = 'sportmen'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    service = Column(UUID(as_uuid=True), ForeignKey("service.id"), nullable=False)
    sportmen = Column(UUID(as_uuid=True), nullable=False)
    amount =  Column(Integer(), nullable=False)