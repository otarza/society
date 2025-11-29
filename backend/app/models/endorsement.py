import uuid
from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, Enum, Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import EndorsementStatus

class Endorsement(Base):
    __tablename__ = "endorsements"

    geder_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    supporter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    status: Mapped[EndorsementStatus] = mapped_column(Enum(EndorsementStatus), nullable=False, default=EndorsementStatus.PENDING)
    
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    approved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    revocation_reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    penalty_applied: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships
    geder: Mapped["User"] = relationship("User", foreign_keys=[geder_id], back_populates="endorsements_given")
    supporter: Mapped["User"] = relationship("User", foreign_keys=[supporter_id], back_populates="endorsement_received")
