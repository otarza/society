import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, ForeignKey, Enum, Integer, Text, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.utils.enums import ElectionType, ElectionScopeType, ElectionStatus

class Election(Base):
    __tablename__ = "elections"

    election_type: Mapped[ElectionType] = mapped_column(Enum(ElectionType), nullable=False)
    scope_type: Mapped[ElectionScopeType] = mapped_column(Enum(ElectionScopeType), nullable=False)
    scope_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ends_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[ElectionStatus] = mapped_column(Enum(ElectionStatus), nullable=False, default=ElectionStatus.SCHEDULED)
    
    winner_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("users.id"), nullable=True)
    total_votes: Mapped[int] = mapped_column(Integer, default=0)

    # Relationships
    winner: Mapped[Optional["User"]] = relationship("User", foreign_keys=[winner_id])
    candidates: Mapped[List["ElectionCandidate"]] = relationship("ElectionCandidate", back_populates="election")
    votes: Mapped[List["Vote"]] = relationship("Vote", back_populates="election")


class ElectionCandidate(Base):
    __tablename__ = "election_candidates"

    election_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("elections.id"), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    statement: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    vote_count: Mapped[int] = mapped_column(Integer, default=0)
    registered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    # Relationships
    election: Mapped["Election"] = relationship("Election", back_populates="candidates")
    user: Mapped["User"] = relationship("User")

    __table_args__ = (
        UniqueConstraint('election_id', 'user_id', name='unique_candidate_per_election'),
    )


class Vote(Base):
    __tablename__ = "votes"

    election_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("elections.id"), nullable=False)
    voter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    candidate_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("election_candidates.id"), nullable=False)
    vote_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    cast_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    # Relationships
    election: Mapped["Election"] = relationship("Election", back_populates="votes")
    voter: Mapped["User"] = relationship("User")
    candidate: Mapped["ElectionCandidate"] = relationship("ElectionCandidate")

    __table_args__ = (
        UniqueConstraint('election_id', 'voter_id', name='unique_vote_per_election'),
    )
