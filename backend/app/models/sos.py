import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import SOSStatus, SOSPriority, HierarchyLevel

class SOSSignal(Base):
    __tablename__ = "sos_signals"

    reporter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    location: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    moral_filter_response: Mapped[str] = mapped_column(Text, nullable=False)
    
    status: Mapped[SOSStatus] = mapped_column(Enum(SOSStatus), nullable=False, default=SOSStatus.PENDING)
    priority: Mapped[SOSPriority] = mapped_column(Enum(SOSPriority), nullable=False, default=SOSPriority.NORMAL)
    
    verifier_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    verification_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    current_level: Mapped[HierarchyLevel] = mapped_column(Enum(HierarchyLevel), nullable=False, default=HierarchyLevel.ATEULI)
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    reporter: Mapped["User"] = relationship("User", foreign_keys=[reporter_id])
    verifier: Mapped[Optional["User"]] = relationship("User", foreign_keys=[verifier_id])
    escalations: Mapped[List["SOSEscalation"]] = relationship("SOSEscalation", back_populates="signal")


class SOSEscalation(Base):
    __tablename__ = "sos_escalations"

    signal_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sos_signals.id"), nullable=False)
    from_level: Mapped[HierarchyLevel] = mapped_column(Enum(HierarchyLevel), nullable=False)
    to_level: Mapped[HierarchyLevel] = mapped_column(Enum(HierarchyLevel), nullable=False)
    escalated_by_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    escalated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    signal: Mapped["SOSSignal"] = relationship("SOSSignal", back_populates="escalations")
    escalated_by: Mapped["User"] = relationship("User")
