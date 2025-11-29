import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, Integer, Text, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import InitiativeCategory, InitiativeStatus, ElectionScopeType

class Initiative(Base):
    __tablename__ = "initiatives"

    creator_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[InitiativeCategory] = mapped_column(Enum(InitiativeCategory), nullable=False)
    
    scope_type: Mapped[ElectionScopeType] = mapped_column(Enum(ElectionScopeType), nullable=False)
    scope_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    
    target_support: Mapped[int] = mapped_column(Integer, nullable=False)
    current_support: Mapped[int] = mapped_column(Integer, default=0)
    
    status: Mapped[InitiativeStatus] = mapped_column(Enum(InitiativeStatus), nullable=False, default=InitiativeStatus.DRAFT)
    assigned_to_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    assigned_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    creator: Mapped["User"] = relationship("User", foreign_keys=[creator_id])
    assigned_to: Mapped[Optional["User"]] = relationship("User", foreign_keys=[assigned_to_id])
    supports: Mapped[List["InitiativeSupport"]] = relationship("InitiativeSupport", back_populates="initiative")


class InitiativeSupport(Base):
    __tablename__ = "initiative_supports"

    initiative_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("initiatives.id"), nullable=False)
    supporter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    supported_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    # Relationships
    initiative: Mapped["Initiative"] = relationship("Initiative", back_populates="supports")
    supporter: Mapped["User"] = relationship("User")

    __table_args__ = (
        UniqueConstraint('initiative_id', 'supporter_id', name='unique_support_per_initiative'),
    )
