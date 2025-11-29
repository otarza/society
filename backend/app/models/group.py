import uuid
from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import GroupStatus

class Ateuli(Base):
    __tablename__ = "ateulis"

    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    territory_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("territories.id"), nullable=False)
    atistavi_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    ormotsdaateuli_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("ormotsdaateulis.id"), nullable=True)
    member_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[GroupStatus] = mapped_column(Enum(GroupStatus), nullable=False, default=GroupStatus.FORMING)

    # Relationships
    territory: Mapped["Territory"] = relationship("Territory", back_populates="ateulis")
    atistavi: Mapped[Optional["User"]] = relationship("User", foreign_keys=[atistavi_id], back_populates="led_ateuli")
    members: Mapped[List["User"]] = relationship("User", foreign_keys="User.ateuli_id", back_populates="ateuli")
    ormotsdaateuli: Mapped[Optional["Ormotsdaateuli"]] = relationship("Ormotsdaateuli", back_populates="ateulis")


class Ormotsdaateuli(Base):
    __tablename__ = "ormotsdaateulis"

    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    territory_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("territories.id"), nullable=False)
    leader_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    aseuli_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("aseulis.id"), nullable=True)
    ateuli_count: Mapped[int] = mapped_column(Integer, default=0)
    member_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[GroupStatus] = mapped_column(Enum(GroupStatus), nullable=False, default=GroupStatus.FORMING)

    # Relationships
    territory: Mapped["Territory"] = relationship("Territory", back_populates="ormotsdaateulis")
    leader: Mapped[Optional["User"]] = relationship("User", foreign_keys=[leader_id], back_populates="led_ormotsdaateuli")
    ateulis: Mapped[List["Ateuli"]] = relationship("Ateuli", back_populates="ormotsdaateuli")
    aseuli: Mapped[Optional["Aseuli"]] = relationship("Aseuli", back_populates="ormotsdaateulis")


class Aseuli(Base):
    __tablename__ = "aseulis"

    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    territory_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("territories.id"), nullable=False)
    asistavi_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    ataseuli_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("ataseulis.id"), nullable=True)
    ormotsdaateuli_count: Mapped[int] = mapped_column(Integer, default=0)
    member_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[GroupStatus] = mapped_column(Enum(GroupStatus), nullable=False, default=GroupStatus.FORMING)

    # Relationships
    territory: Mapped["Territory"] = relationship("Territory", back_populates="aseulis")
    asistavi: Mapped[Optional["User"]] = relationship("User", foreign_keys=[asistavi_id], back_populates="led_aseuli")
    ormotsdaateulis: Mapped[List["Ormotsdaateuli"]] = relationship("Ormotsdaateuli", back_populates="aseuli")
    ataseuli: Mapped[Optional["Ataseuli"]] = relationship("Ataseuli", back_populates="aseulis")


class Ataseuli(Base):
    __tablename__ = "ataseulis"

    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    territory_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("territories.id"), nullable=False)
    atasistavi_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    aseuli_count: Mapped[int] = mapped_column(Integer, default=0)
    member_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[GroupStatus] = mapped_column(Enum(GroupStatus), nullable=False, default=GroupStatus.FORMING)
    budget_amount: Mapped[float] = mapped_column(Numeric(15, 2), default=0)

    # Relationships
    territory: Mapped["Territory"] = relationship("Territory", back_populates="ataseulis")
    atasistavi: Mapped[Optional["User"]] = relationship("User", foreign_keys=[atasistavi_id], back_populates="led_ataseuli")
    aseulis: Mapped[List["Aseuli"]] = relationship("Aseuli", back_populates="ataseuli")
