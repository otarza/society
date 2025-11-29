# API Architecture - Girchi Digital Polis

## Overview

This document defines the complete API architecture for the Girchi Digital Polis backend, including endpoint specifications, authentication flows, and integration patterns.

## Architecture Principles

### RESTful Design
- Resource-based URLs
- HTTP methods for CRUD operations
- Stateless communication
- Proper HTTP status codes
- HATEOAS where applicable

### API Versioning
- URL-based versioning: `/api/v1/`
- Backward compatibility maintained for at least 2 versions
- Deprecation notices in headers

### Response Format
All responses follow a consistent structure:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "timestamp": "2025-11-28T14:00:00Z",
    "request_id": "uuid"
  }
}
```

Error responses:
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": { ... }
  },
  "meta": {
    "timestamp": "2025-11-28T14:00:00Z",
    "request_id": "uuid"
  }
}
```

## Authentication & Authorization

### Authentication Flow

#### 1. Phone Verification (Registration/Login)
```
POST /api/v1/auth/send-verification-code
POST /api/v1/auth/verify-phone
```

#### 2. JWT Token Management
- Access Token: 15 minutes expiry
- Refresh Token: 30 days expiry
- Stored in HTTP-only cookies (web) or secure storage (mobile)

#### 3. Token Refresh
```
POST /api/v1/auth/refresh
```

### Authorization Levels

1. **Public**: No authentication required
2. **Authenticated**: Valid JWT token
3. **Verified**: Completed onboarding
4. **GeDer**: Role = 'geder'
5. **Active Member**: Status = 'active'
6. **Leader**: Has leadership position
7. **Admin**: System administrator

## API Endpoints

### 1. Authentication & User Management

#### Auth Endpoints

```
POST   /api/v1/auth/send-verification-code
POST   /api/v1/auth/verify-phone
POST   /api/v1/auth/refresh
POST   /api/v1/auth/logout
```

**POST /api/v1/auth/send-verification-code**
```json
Request:
{
  "phone_number": "+995555123456"
}

Response:
{
  "success": true,
  "data": {
    "verification_id": "uuid",
    "expires_at": "2025-11-28T14:05:00Z"
  }
}
```

**POST /api/v1/auth/verify-phone**
```json
Request:
{
  "verification_id": "uuid",
  "code": "123456",
  "device_fingerprint": {
    "fingerprint_hash": "hash",
    "device_type": "ios",
    "device_model": "iPhone 15",
    "os_version": "17.0",
    "app_version": "1.0.0"
  }
}

Response:
{
  "success": true,
  "data": {
    "access_token": "jwt_token",
    "refresh_token": "jwt_token",
    "user": {
      "id": "uuid",
      "phone_number": "+995555123456",
      "role": "unverified",
      "onboarding_completed": false
    }
  }
}
```

#### User Endpoints

```
GET    /api/v1/users/me
PATCH  /api/v1/users/me
POST   /api/v1/users/me/complete-onboarding
GET    /api/v1/users/{user_id}
GET    /api/v1/users/search
```

**GET /api/v1/users/me**
```json
Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "phone_number": "+995555123456",
    "role": "geder",
    "status": "active",
    "is_diaspora": false,
    "territory": {
      "id": "uuid",
      "name": "თბილისი - ვაკე",
      "type": "electoral_district"
    },
    "ateuli": {
      "id": "uuid",
      "name": "ვაკის ათეული #1",
      "member_count": 10
    },
    "tavdebi": null,
    "constitution_agreed_at": "2025-11-28T14:00:00Z",
    "onboarding_completed_at": "2025-11-28T14:00:00Z",
    "created_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/users/me/complete-onboarding**
```json
Request:
{
  "personal_id": "01234567890",
  "is_geder": true,
  "ged_number": "GED123456",
  "status": "active",
  "motivation": "I want to participate in building a free society",
  "constitution_agreed": true,
  "is_diaspora": false,
  "territory_id": "uuid"
}

Response:
{
  "success": true,
  "data": {
    "user": { ... },
    "next_steps": [
      "join_ateuli",
      "find_tavdebi"
    ]
  }
}
```

---

### 2. Territory & Geographic

```
GET    /api/v1/territories
GET    /api/v1/territories/{territory_id}
GET    /api/v1/territories/{territory_id}/ateulis
GET    /api/v1/territories/{territory_id}/members
GET    /api/v1/territories/{territory_id}/statistics
```

**GET /api/v1/territories**
```json
Query Parameters:
- type: electoral_district | region | municipality
- parent_id: uuid
- search: string

Response:
{
  "success": true,
  "data": {
    "territories": [
      {
        "id": "uuid",
        "name": "თბილისი - ვაკე",
        "name_en": "Tbilisi - Vake",
        "type": "electoral_district",
        "code": "TB-VAKE-01",
        "member_count": 150,
        "ateuli_count": 15
      }
    ]
  },
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20
  }
}
```

---

### 3. Ateuli & Group Management

```
GET    /api/v1/ateulis
POST   /api/v1/ateulis
GET    /api/v1/ateulis/{ateuli_id}
PATCH  /api/v1/ateulis/{ateuli_id}
POST   /api/v1/ateulis/{ateuli_id}/join
POST   /api/v1/ateulis/{ateuli_id}/leave
GET    /api/v1/ateulis/{ateuli_id}/members
```

**POST /api/v1/ateulis**
```json
Request:
{
  "name": "ვაკის ათეული #1",
  "territory_id": "uuid"
}

Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "ვაკის ათეული #1",
    "territory_id": "uuid",
    "member_count": 1,
    "status": "forming",
    "created_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/ateulis/{ateuli_id}/join**
```json
Request:
{
  "message": "I'd like to join this group"
}

Response:
{
  "success": true,
  "data": {
    "ateuli": { ... },
    "membership": {
      "joined_at": "2025-11-28T14:00:00Z",
      "role": "member"
    }
  }
}
```

---

### 4. Endorsement System

```
GET    /api/v1/endorsements/available-geders
POST   /api/v1/endorsements/request
GET    /api/v1/endorsements/my-requests
GET    /api/v1/endorsements/pending-approvals
POST   /api/v1/endorsements/{endorsement_id}/approve
POST   /api/v1/endorsements/{endorsement_id}/reject
POST   /api/v1/endorsements/{endorsement_id}/revoke
GET    /api/v1/endorsements/my-supporters
```

**GET /api/v1/endorsements/available-geders**
```json
Query Parameters:
- territory_id: uuid
- search: string

Response:
{
  "success": true,
  "data": {
    "geders": [
      {
        "id": "uuid",
        "ateuli": {
          "id": "uuid",
          "name": "ვაკის ათეული #1"
        },
        "available_slots": 3,
        "total_slots": 10,
        "endorsement_count": 7
      }
    ]
  }
}
```

**POST /api/v1/endorsements/request**
```json
Request:
{
  "geder_id": "uuid",
  "message": "I would like to join the society"
}

Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "geder_id": "uuid",
    "supporter_id": "uuid",
    "status": "pending",
    "requested_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/endorsements/{endorsement_id}/approve**
```json
Response:
{
  "success": true,
  "data": {
    "endorsement": {
      "id": "uuid",
      "status": "approved",
      "approved_at": "2025-11-28T14:00:00Z"
    },
    "supporter": {
      "id": "uuid",
      "role": "supporter",
      "tavdebi_id": "uuid"
    }
  }
}
```

---

### 5. Elections & Voting

```
GET    /api/v1/elections
POST   /api/v1/elections
GET    /api/v1/elections/{election_id}
GET    /api/v1/elections/{election_id}/candidates
POST   /api/v1/elections/{election_id}/register-candidate
POST   /api/v1/elections/{election_id}/vote
GET    /api/v1/elections/{election_id}/results
GET    /api/v1/elections/my-elections
```

**GET /api/v1/elections**
```json
Query Parameters:
- election_type: atistavi | ormotsdaatistavi | asistavi | atasistavi | parliamentary
- status: scheduled | active | completed
- scope_type: ateuli | ormotsdaateuli | aseuli | ataseuli | national
- scope_id: uuid

Response:
{
  "success": true,
  "data": {
    "elections": [
      {
        "id": "uuid",
        "election_type": "atistavi",
        "scope_type": "ateuli",
        "scope_id": "uuid",
        "title": "ათისთავის არჩევნები - ვაკის ათეული #1",
        "starts_at": "2025-12-01T09:00:00Z",
        "ends_at": "2025-12-01T18:00:00Z",
        "status": "scheduled",
        "candidate_count": 3,
        "total_votes": 0
      }
    ]
  }
}
```

**POST /api/v1/elections/{election_id}/vote**
```json
Request:
{
  "candidate_id": "uuid"
}

Response:
{
  "success": true,
  "data": {
    "vote": {
      "id": "uuid",
      "election_id": "uuid",
      "vote_hash": "verification_hash",
      "cast_at": "2025-11-28T14:00:00Z"
    }
  }
}
```

**GET /api/v1/elections/{election_id}/results**
```json
Response:
{
  "success": true,
  "data": {
    "election": {
      "id": "uuid",
      "title": "ათისთავის არჩევნები - ვაკის ათეული #1",
      "status": "completed",
      "total_votes": 10
    },
    "results": [
      {
        "candidate": {
          "id": "uuid",
          "name": "გიორგი მელაძე"
        },
        "vote_count": 7,
        "percentage": 70.0,
        "is_winner": true
      },
      {
        "candidate": {
          "id": "uuid",
          "name": "ნინო ბერიძე"
        },
        "vote_count": 3,
        "percentage": 30.0,
        "is_winner": false
      }
    ]
  }
}
```

---

### 6. SOS System

```
POST   /api/v1/sos/signals
GET    /api/v1/sos/signals
GET    /api/v1/sos/signals/{signal_id}
PATCH  /api/v1/sos/signals/{signal_id}
POST   /api/v1/sos/signals/{signal_id}/verify
POST   /api/v1/sos/signals/{signal_id}/escalate
POST   /api/v1/sos/signals/{signal_id}/resolve
GET    /api/v1/sos/signals/pending-verification
```

**POST /api/v1/sos/signals**
```json
Request:
{
  "title": "უსამართლობა სამსახურში",
  "description": "დეტალური აღწერა...",
  "location": "თბილისი, ვაკე",
  "moral_filter_response": "დიახ, ვარ პატიოსანი, მშრომელი ადამიანი"
}

Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "უსამართლობა სამსახურში",
    "status": "pending",
    "priority": "normal",
    "current_level": "ateuli",
    "created_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/sos/signals/{signal_id}/verify**
```json
Request:
{
  "is_legitimate": true,
  "verification_notes": "ვერიფიცირებულია, რეალური შემთხვევაა",
  "priority": "high"
}

Response:
{
  "success": true,
  "data": {
    "signal": {
      "id": "uuid",
      "status": "verified",
      "priority": "high",
      "verifier_id": "uuid",
      "verified_at": "2025-11-28T14:00:00Z"
    }
  }
}
```

**POST /api/v1/sos/signals/{signal_id}/escalate**
```json
Request:
{
  "to_level": "ormotsdaateuli",
  "notes": "საჭიროებს უფრო მაღალი დონის ყურადღებას"
}

Response:
{
  "success": true,
  "data": {
    "signal": {
      "id": "uuid",
      "status": "escalated",
      "current_level": "ormotsdaateuli"
    },
    "escalation": {
      "id": "uuid",
      "from_level": "ateuli",
      "to_level": "ormotsdaateuli",
      "escalated_at": "2025-11-28T14:00:00Z"
    }
  }
}
```

---

### 7. Initiatives & Petitions

```
POST   /api/v1/initiatives
GET    /api/v1/initiatives
GET    /api/v1/initiatives/{initiative_id}
PATCH  /api/v1/initiatives/{initiative_id}
POST   /api/v1/initiatives/{initiative_id}/support
DELETE /api/v1/initiatives/{initiative_id}/support
POST   /api/v1/initiatives/{initiative_id}/assign
POST   /api/v1/initiatives/{initiative_id}/complete
GET    /api/v1/initiatives/my-initiatives
GET    /api/v1/initiatives/assigned-to-me
```

**POST /api/v1/initiatives**
```json
Request:
{
  "title": "სკოლის დაფუძნება ვაკეში",
  "description": "დეტალური აღწერა...",
  "category": "education",
  "scope_type": "aseuli",
  "scope_id": "uuid",
  "target_support": 50
}

Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "სკოლის დაფუძნება ვაკეში",
    "category": "education",
    "status": "active",
    "target_support": 50,
    "current_support": 0,
    "progress_percentage": 0,
    "created_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/initiatives/{initiative_id}/support**
```json
Request:
{
  "comment": "მხარს ვუჭერ ამ ინიციატივას"
}

Response:
{
  "success": true,
  "data": {
    "initiative": {
      "id": "uuid",
      "current_support": 25,
      "progress_percentage": 50,
      "status": "active"
    },
    "support": {
      "id": "uuid",
      "supported_at": "2025-11-28T14:00:00Z"
    }
  }
}
```

---

### 8. Arbitration

```
POST   /api/v1/arbitration/cases
GET    /api/v1/arbitration/cases
GET    /api/v1/arbitration/cases/{case_id}
POST   /api/v1/arbitration/cases/{case_id}/assign
POST   /api/v1/arbitration/cases/{case_id}/resolve
GET    /api/v1/arbitration/my-cases
GET    /api/v1/arbitration/assigned-to-me
```

**POST /api/v1/arbitration/cases**
```json
Request:
{
  "defendant_id": "uuid",
  "title": "დავა მეზობელთან",
  "description": "დეტალური აღწერა..."
}

Response:
{
  "success": true,
  "data": {
    "id": "uuid",
    "case_number": "ARB-2025-001234",
    "plaintiff_id": "uuid",
    "defendant_id": "uuid",
    "title": "დავა მეზობელთან",
    "status": "pending",
    "created_at": "2025-11-28T14:00:00Z"
  }
}
```

**POST /api/v1/arbitration/cases/{case_id}/resolve**
```json
Request:
{
  "resolution": "გადაწყვეტილების დეტალური აღწერა..."
}

Response:
{
  "success": true,
  "data": {
    "case": {
      "id": "uuid",
      "status": "resolved",
      "resolution": "გადაწყვეტილების დეტალური აღწერა...",
      "resolved_at": "2025-11-28T14:00:00Z"
    }
  }
}
```

---

### 9. Hierarchy & Leadership

```
GET    /api/v1/hierarchy/overview
GET    /api/v1/hierarchy/ormotsdaateulis
GET    /api/v1/hierarchy/aseulis
GET    /api/v1/hierarchy/ataseulis
GET    /api/v1/hierarchy/satatbiro
GET    /api/v1/hierarchy/my-position
```

**GET /api/v1/hierarchy/overview**
```json
Response:
{
  "success": true,
  "data": {
    "total_members": 15000,
    "total_ateulis": 1500,
    "total_ormotsdaateulis": 300,
    "total_aseulis": 150,
    "total_ataseulis": 15,
    "hierarchy_levels": [
      {
        "level": "ataseuli",
        "count": 15,
        "member_count": 15000
      },
      {
        "level": "aseuli",
        "count": 150,
        "member_count": 15000
      }
    ]
  }
}
```

**GET /api/v1/hierarchy/my-position**
```json
Response:
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "role": "geder",
      "status": "active"
    },
    "positions": [
      {
        "type": "atistavi",
        "group_id": "uuid",
        "group_name": "ვაკის ათეული #1",
        "elected_at": "2025-11-01T14:00:00Z"
      }
    ],
    "ateuli": {
      "id": "uuid",
      "name": "ვაკის ათეული #1",
      "member_count": 10
    },
    "hierarchy_path": [
      {
        "level": "ateuli",
        "id": "uuid",
        "name": "ვაკის ათეული #1"
      },
      {
        "level": "ormotsdaateuli",
        "id": "uuid",
        "name": "ვაკის ორმოცდაათეული #1"
      }
    ]
  }
}
```

---

### 10. Gamification & Progress

```
GET    /api/v1/gamification/progress
GET    /api/v1/gamification/achievements
GET    /api/v1/gamification/leaderboard
GET    /api/v1/gamification/unlocked-capabilities
```

**GET /api/v1/gamification/progress**
```json
Response:
{
  "success": true,
  "data": {
    "current_level": {
      "type": "aseuli",
      "member_count": 100,
      "required_count": 100,
      "progress_percentage": 100
    },
    "next_level": {
      "type": "ataseuli",
      "member_count": 100,
      "required_count": 1000,
      "progress_percentage": 10,
      "members_needed": 900
    },
    "unlocked_capabilities": [
      "arbitration",
      "tv_time_basic",
      "local_initiatives"
    ],
    "next_capabilities": [
      "tv_time_extended",
      "budget_allocation"
    ]
  }
}
```

---

### 11. Notifications

```
GET    /api/v1/notifications
PATCH  /api/v1/notifications/{notification_id}/read
POST   /api/v1/notifications/mark-all-read
DELETE /api/v1/notifications/{notification_id}
```

**GET /api/v1/notifications**
```json
Query Parameters:
- unread_only: boolean
- type: string
- limit: integer
- offset: integer

Response:
{
  "success": true,
  "data": {
    "notifications": [
      {
        "id": "uuid",
        "type": "election_started",
        "title": "ახალი არჩევნები დაიწყო",
        "message": "ათისთავის არჩევნები თქვენს ათეულში",
        "data": {
          "election_id": "uuid"
        },
        "read_at": null,
        "created_at": "2025-11-28T14:00:00Z"
      }
    ],
    "unread_count": 5
  },
  "meta": {
    "total": 50,
    "limit": 20,
    "offset": 0
  }
}
```

---

### 12. Statistics & Analytics

```
GET    /api/v1/statistics/platform
GET    /api/v1/statistics/territory/{territory_id}
GET    /api/v1/statistics/ateuli/{ateuli_id}
GET    /api/v1/statistics/user/{user_id}
```

**GET /api/v1/statistics/platform**
```json
Response:
{
  "success": true,
  "data": {
    "total_users": 15000,
    "verified_users": 14500,
    "geders": 10000,
    "supporters": 4500,
    "active_members": 8000,
    "passive_members": 6500,
    "total_ateulis": 1500,
    "active_elections": 25,
    "pending_sos_signals": 12,
    "active_initiatives": 45,
    "growth_rate": {
      "daily": 150,
      "weekly": 1000,
      "monthly": 4000
    }
  }
}
```

---

## WebSocket Events

For real-time updates, the platform uses WebSocket connections.

### Connection
```
ws://api.domain.com/ws?token=jwt_token
```

### Event Types

#### 1. Election Updates
```json
{
  "event": "election.started",
  "data": {
    "election_id": "uuid",
    "election_type": "atistavi",
    "starts_at": "2025-11-28T14:00:00Z"
  }
}
```

#### 2. SOS Signal Updates
```json
{
  "event": "sos.new_signal",
  "data": {
    "signal_id": "uuid",
    "priority": "high",
    "current_level": "ateuli"
  }
}
```

#### 3. Initiative Updates
```json
{
  "event": "initiative.support_threshold_reached",
  "data": {
    "initiative_id": "uuid",
    "current_support": 50,
    "target_support": 50
  }
}
```

#### 4. Notification
```json
{
  "event": "notification.new",
  "data": {
    "notification_id": "uuid",
    "type": "endorsement_approved",
    "title": "თქვენი ენდორსმენტი დამტკიცდა"
  }
}
```

---

## Error Codes

### Authentication Errors (1xxx)
- `1001`: Invalid credentials
- `1002`: Token expired
- `1003`: Token invalid
- `1004`: Insufficient permissions
- `1005`: Account not verified

### Validation Errors (2xxx)
- `2001`: Missing required field
- `2002`: Invalid field format
- `2003`: Field value out of range
- `2004`: Duplicate entry

### Business Logic Errors (3xxx)
- `3001`: Endorsement limit reached
- `3002`: Already voted in election
- `3003`: Election not active
- `3004`: Not eligible to vote
- `3005`: Group is full
- `3006`: Already member of group
- `3007`: Cannot endorse yourself
- `3008`: Invalid hierarchy level

### Resource Errors (4xxx)
- `4001`: Resource not found
- `4002`: Resource already exists
- `4003`: Resource deleted

### System Errors (5xxx)
- `5001`: Internal server error
- `5002`: Database error
- `5003`: External service error

---

## Rate Limiting

### Default Limits
- **Anonymous**: 100 requests/hour
- **Authenticated**: 1000 requests/hour
- **Leaders**: 5000 requests/hour

### Specific Endpoints
- **POST /api/v1/auth/send-verification-code**: 5 requests/hour per phone
- **POST /api/v1/sos/signals**: 10 requests/day per user
- **POST /api/v1/initiatives**: 5 requests/day per user

### Headers
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640000000
```

---

## Pagination

All list endpoints support pagination:

### Query Parameters
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 20, max: 100)
- `sort_by`: Field to sort by
- `sort_order`: asc | desc

### Response Meta
```json
{
  "meta": {
    "total": 1000,
    "page": 1,
    "per_page": 20,
    "total_pages": 50,
    "has_next": true,
    "has_prev": false
  }
}
```

---

## Filtering & Search

### Common Filters
- `created_after`: ISO 8601 timestamp
- `created_before`: ISO 8601 timestamp
- `status`: Enum value
- `search`: Full-text search

### Example
```
GET /api/v1/initiatives?category=education&status=active&search=school&page=1&per_page=20
```

---

## Caching Strategy

### Cache Headers
```
Cache-Control: public, max-age=300
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```

### Cached Endpoints
- Territory data: 24 hours
- User profile: 1 hour
- Statistics: 5 minutes
- Election results (completed): 1 week

---

## API Documentation

### Auto-Generated Docs
- **Swagger UI**: `/api/v1/docs`
- **ReDoc**: `/api/v1/redoc`
- **OpenAPI JSON**: `/api/v1/openapi.json`

### Postman Collection
Available at: `/api/v1/postman-collection.json`

---

## Security Considerations

### HTTPS Only
All API endpoints require HTTPS in production.

### CORS
Configured for mobile app domains and web app domains.

### Input Validation
- All inputs validated using Pydantic models
- SQL injection prevention via ORM
- XSS prevention via output encoding

### Sensitive Data
- Personal IDs never returned in responses
- Phone numbers masked in public endpoints
- GeD numbers encrypted

### Audit Logging
All sensitive operations logged:
- Authentication attempts
- Voting actions
- Endorsements
- Leadership changes
- SOS signals
