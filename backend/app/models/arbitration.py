import uuid
from datetime import datetime
from typing import Optional
from sqlalchemy import String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import ArbitrationStatus

class ArbitrationCase(Base):
    __tablename__ = "arbitration_cases"

    case_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    plaintiff_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    defendant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    arbitrator_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[ArbitrationStatus] = mapped_column(Enum(ArbitrationStatus), nullable=False, default=ArbitrationStatus.PENDING)
    
    resolution: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    plaintiff: Mapped["User"] = relationship("User", foreign_keys=[plaintiff_id])
    defendant: Mapped["User"] = relationship("User", foreign_keys=[defendant_id])
    arbitrator: Mapped[Optional["User"]] = relationship("User", foreign_keys=[arbitrator_id])
