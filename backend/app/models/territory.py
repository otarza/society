from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import TerritoryType

class Territory(Base):
    __tablename__ = "territories"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    name_en: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    type: Mapped[TerritoryType] = mapped_column(Enum(TerritoryType), nullable=False)
    parent_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("territories.id"), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(50), unique=True, nullable=True)
    
    # Hierarchical relationship
    parent: Mapped[Optional["Territory"]] = relationship("Territory", remote_side="Territory.id", back_populates="children")
    children: Mapped[List["Territory"]] = relationship("Territory", back_populates="parent")
    
    # Relationships
    users: Mapped[List["User"]] = relationship("User", back_populates="territory")
    ateulis: Mapped[List["Ateuli"]] = relationship("Ateuli", back_populates="territory")
    ormotsdaateulis: Mapped[List["Ormotsdaateuli"]] = relationship("Ormotsdaateuli", back_populates="territory")
    aseulis: Mapped[List["Aseuli"]] = relationship("Aseuli", back_populates="territory")
    ataseulis: Mapped[List["Ataseuli"]] = relationship("Ataseuli", back_populates="territory")

    def __repr__(self):
        return f"<Territory {self.name} ({self.type})>"
