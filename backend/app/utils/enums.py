from enum import Enum

class UserRole(str, Enum):
    UNVERIFIED = "unverified"
    GEDER = "geder"
    SUPPORTER = "supporter"

class UserStatus(str, Enum):
    PASSIVE = "passive"
    ACTIVE = "active"

class EndorsementStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    REVOKED = "revoked"

class TerritoryType(str, Enum):
    ELECTORAL_DISTRICT = "electoral_district"
    REGION = "region"
    MUNICIPALITY = "municipality"

class GroupStatus(str, Enum):
    FORMING = "forming"
    ACTIVE = "active"
    INACTIVE = "inactive"

class ElectionType(str, Enum):
    ATISTAVI = "atistavi"
    ORMOTSDAATISTAVI = "ormotsdaatistavi"
    ASISTAVI = "asistavi"
    ATASISTAVI = "atasistavi"
    PARLIAMENTARY = "parliamentary"

class ElectionScopeType(str, Enum):
    ATEULI = "ateuli"
    ORMOTSDAATEULI = "ormotsdaateuli"
    ASEULI = "aseuli"
    ATASEULI = "ataseuli"
    NATIONAL = "national"

class ElectionStatus(str, Enum):
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class SOSStatus(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    ESCALATED = "escalated"
    RESOLVED = "resolved"
    REJECTED = "rejected"

class SOSPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"

class HierarchyLevel(str, Enum):
    ATEULI = "ateuli"
    ORMOTSDAATEULI = "ormotsdaateuli"
    ASEULI = "aseuli"
    ATASEULI = "ataseuli"
    MEDIA = "media"

class InitiativeCategory(str, Enum):
    EDUCATION = "education"
    INFRASTRUCTURE = "infrastructure"
    SOCIAL = "social"
    ECONOMIC = "economic"
    OTHER = "other"

class InitiativeStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    ACHIEVED = "achieved"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    REJECTED = "rejected"

class ArbitrationStatus(str, Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    APPEALED = "appealed"
