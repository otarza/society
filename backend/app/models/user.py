import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import UserRole, UserStatus

class User(Base):
    __tablename__ = "users"

    phone_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    phone_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    personal_id_hash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False, default=UserRole.UNVERIFIED)
    status: Mapped[Optional[UserStatus]] = mapped_column(Enum(UserStatus), nullable=True)
    is_diaspora: Mapped[bool] = mapped_column(Boolean, default=False)
    
    territory_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("territories.id"), nullable=True)
    ateuli_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("ateulis.id"), nullable=True)
    tavdebi_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    
    constitution_agreed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    onboarding_completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    onboarding_motivation: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    territory: Mapped[Optional["Territory"]] = relationship("Territory", back_populates="users")
    ateuli: Mapped[Optional["Ateuli"]] = relationship("Ateuli", back_populates="members", foreign_keys=[ateuli_id])
    
    # Self-referential relationship for Tavdebi (Endorser)
    tavdebi: Mapped[Optional["User"]] = relationship("User", remote_side="User.id", back_populates="endorsed_supporters")
    endorsed_supporters: Mapped[List["User"]] = relationship("User", back_populates="tavdebi")
    
    # One-to-One relationships
    ged_verification: Mapped[Optional["GeDVerification"]] = relationship("GeDVerification", back_populates="user", uselist=False)
    
    # One-to-Many relationships
    device_fingerprints: Mapped[List["DeviceFingerprint"]] = relationship("DeviceFingerprint", back_populates="user")
    endorsements_given: Mapped[List["Endorsement"]] = relationship("Endorsement", foreign_keys="Endorsement.geder_id", back_populates="geder")
    endorsement_received: Mapped[Optional["Endorsement"]] = relationship("Endorsement", foreign_keys="Endorsement.supporter_id", back_populates="supporter", uselist=False)
    
    # Leadership relationships
    led_ateuli: Mapped[Optional["Ateuli"]] = relationship("Ateuli", back_populates="atistavi", foreign_keys="Ateuli.atistavi_id")
    led_ormotsdaateuli: Mapped[Optional["Ormotsdaateuli"]] = relationship("Ormotsdaateuli", back_populates="leader", foreign_keys="Ormotsdaateuli.leader_id")
    led_aseuli: Mapped[Optional["Aseuli"]] = relationship("Aseuli", back_populates="asistavi", foreign_keys="Aseuli.asistavi_id")
    led_ataseuli: Mapped[Optional["Ataseuli"]] = relationship("Ataseuli", back_populates="atasistavi", foreign_keys="Ataseuli.atasistavi_id")

    def __repr__(self):
        return f"<User {self.phone_number} ({self.role})>"


class GeDVerification(Base):
    __tablename__ = "ged_verifications"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    ged_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    verified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    verified_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="ged_verification")


class DeviceFingerprint(Base):
    __tablename__ = "device_fingerprints"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    fingerprint_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    device_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    device_model: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    os_version: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    app_version: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    first_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship("User", back_populates="device_fingerprints")
