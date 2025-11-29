# Technical Requirements - Girchi Digital Polis

## Executive Summary

The Girchi Digital Polis is a decentralized society management platform that enables self-governance through a hierarchical representative system. The platform supports three user roles (Unverified Users, GeDers, Supporters) with two status levels (Passive/Active members), implements a bottom-up decision-making process, and includes gamification elements to encourage growth.

## Core Concepts

### 1. User Roles

#### Unverified User
- Newly registered person who hasn't completed verification
- Limited functionality until verification is complete
- Can browse but cannot participate in governance

#### GeDer (ჯედერი)
- Verified GeD (membership card) holder
- Core member of the system
- Can vote, run for leadership positions, and endorse supporters
- Each GeDer has an endorsement limit (5-10 people)

#### Supporter (Endorsed by Tavdebi)
- User without GeD card
- Must be endorsed by a GeDer ("Tavdebi" - guarantor)
- Becomes full member with voting rights after endorsement
- Linked to their Tavdebi for accountability

### 2. Member Status

#### Passive Member
- Confirms agreement with Girchi constitution
- Willing to participate in elections
- Can vote but cannot become a leader (Atistavi)

#### Active Member
- All passive member rights plus:
- Publicly declares willingness to express positions
- Eligible to become Atistavi (leader of 10)

### 3. Hierarchical Structure

The system implements a military-inspired hierarchy:

- **Ateuli** (Group of 10): 10 members
- **Atistavi** (Leader of 10): Elected by their Ateuli
- **Ormotsdaatistavi** (Leader of 50): Elected by 5 Atistavis
- **Asistavi** (Leader of 100): Elected by 10 Atistavis  
- **Atasistavi** (Leader of 1000): Elected by 10 Asistavis
- **Satatbiro** (Council): Composed of all Atasistavis

### 4. Key Features

#### Registration & Verification
- Phone number verification (mandatory)
- Personal ID number for uniqueness
- Device fingerprinting to prevent duplicates/fakes
- GeD database verification for GeDers

#### Territory-Based Organization
- Users automatically placed on map by electoral district
- GeDers can join existing Ateuli or create new ones (if enough members)
- Supporters must find a Tavdebi to join

#### Elections
- Direct voting within each level
- Only Active members can run for Atistavi
- Higher-level leaders elected by lower-level leaders
- Parliamentary list voting remains unchanged (all GeDers vote)

#### SOS System
- Emergency button for injustice cases
- Moral filter question to verify legitimacy
- Signal goes to local Atistavi for verification
- Verified signals escalate through hierarchy
- Can reach television if needed

#### Initiatives & Petitions
- Any member can start local initiatives
- Sufficient support requires representative action
- Examples: organizing school establishment

#### Arbitration
- Members can request arbitration from representatives
- Dispute resolution within the community

#### Gamification
- Visual progress indicators
- Level unlocks new capabilities:
  - Increased TV time
  - Arbitration rights
  - Eventually: own budget
- Motivation cycle: More members → New level → More rights/budget → More motivation to recruit

### 5. Security & Accountability

#### Fake Prevention
- Tavdebi responsible for endorsed supporters
- Fake/malicious supporter results in:
  - Loss of endorsement rights for Tavdebi
  - GeD penalty for Tavdebi
- Cases judged by Ormotsdaatistavis, Asistavis, and Atasistavis
- Self-regulating network

#### Diaspora Support
- Emigrants registered as separate category
- Don't participate in local hierarchy
- Maintain connection to community

## Technical Requirements

### Functional Requirements

#### FR-1: User Management
- FR-1.1: Phone number verification
- FR-1.2: Personal ID uniqueness check
- FR-1.3: Device fingerprinting
- FR-1.4: GeD database integration
- FR-1.5: User role management (Unverified/GeDer/Supporter)
- FR-1.6: User status management (Passive/Active)
- FR-1.7: Diaspora user flagging

#### FR-2: Territory Management
- FR-2.1: Electoral district mapping
- FR-2.2: Automatic user placement by location
- FR-2.3: Ateuli (group) creation and management
- FR-2.4: Territory-based user discovery

#### FR-3: Endorsement System
- FR-3.1: Tavdebi endorsement workflow
- FR-3.2: Endorsement limit tracking per GeDer
- FR-3.3: Endorsement request/approval process
- FR-3.4: Endorsement revocation
- FR-3.5: Penalty system for fake endorsements

#### FR-4: Hierarchical Organization
- FR-4.1: Ateuli formation (groups of 10)
- FR-4.2: Automatic hierarchy level calculation
- FR-4.3: Leader position management
- FR-4.4: Hierarchy visualization

#### FR-5: Elections & Voting
- FR-5.1: Atistavi election (direct voting by Ateuli)
- FR-5.2: Higher-level leader elections
- FR-5.3: Parliamentary list voting
- FR-5.4: Vote counting and result calculation
- FR-5.5: Election eligibility verification
- FR-5.6: Voting period management

#### FR-6: SOS System
- FR-6.1: SOS signal creation
- FR-6.2: Moral filter questionnaire
- FR-6.3: Signal routing to local Atistavi
- FR-6.4: Signal verification workflow
- FR-6.5: Signal escalation through hierarchy
- FR-6.6: Signal status tracking

#### FR-7: Initiatives & Petitions
- FR-7.1: Initiative creation
- FR-7.2: Initiative support/voting
- FR-7.3: Support threshold configuration
- FR-7.4: Initiative assignment to representatives
- FR-7.5: Initiative status tracking

#### FR-8: Arbitration
- FR-8.1: Arbitration request creation
- FR-8.2: Arbitration case assignment
- FR-8.3: Arbitration resolution workflow
- FR-8.4: Case history tracking

#### FR-9: Gamification
- FR-9.1: Progress tracking per territory/group
- FR-9.2: Level calculation based on member count
- FR-9.3: Capability unlocking system
- FR-9.4: Visual progress indicators
- FR-9.5: Achievement/milestone notifications

#### FR-10: Constitution & Onboarding
- FR-10.1: Constitution agreement workflow
- FR-10.2: Onboarding questionnaire
- FR-10.3: Member commitment level selection

### Non-Functional Requirements

#### NFR-1: Security
- NFR-1.1: End-to-end encryption for sensitive data
- NFR-1.2: Secure authentication (JWT tokens)
- NFR-1.3: Rate limiting to prevent abuse
- NFR-1.4: Audit logging for all critical actions
- NFR-1.5: GDPR compliance for personal data

#### NFR-2: Performance
- NFR-2.1: API response time < 200ms for 95% of requests
- NFR-2.2: Support for 100,000+ concurrent users
- NFR-2.3: Database query optimization
- NFR-2.4: Caching strategy for frequently accessed data

#### NFR-3: Scalability
- NFR-3.1: Horizontal scaling capability
- NFR-3.2: Database sharding strategy
- NFR-3.3: Microservices-ready architecture

#### NFR-4: Reliability
- NFR-4.1: 99.9% uptime SLA
- NFR-4.2: Automated backup system
- NFR-4.3: Disaster recovery plan
- NFR-4.4: Health monitoring and alerting

#### NFR-5: Maintainability
- NFR-5.1: Comprehensive API documentation
- NFR-5.2: Code coverage > 80%
- NFR-5.3: Automated testing pipeline
- NFR-5.4: Clear code structure and naming conventions

#### NFR-6: Usability
- NFR-6.1: RESTful API design
- NFR-6.2: Consistent error messages
- NFR-6.3: API versioning strategy
- NFR-6.4: Comprehensive API documentation (OpenAPI/Swagger)

## Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15+ (primary data store)
- **Cache**: Redis (session management, caching)
- **Task Queue**: Celery with Redis broker (async tasks)
- **ORM**: SQLAlchemy 2.0+
- **Migrations**: Alembic
- **Authentication**: JWT with PyJWT
- **Validation**: Pydantic V2

### DevOps & Infrastructure
- **Containerization**: Docker
- **Orchestration**: Docker Compose (dev), Kubernetes (production)
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

### Testing
- **Unit Tests**: pytest
- **Integration Tests**: pytest with TestClient
- **Load Testing**: Locust
- **API Testing**: pytest + httpx

### Documentation
- **API Docs**: FastAPI auto-generated (Swagger/ReDoc)
- **Architecture**: Mermaid diagrams
- **Code Docs**: Docstrings (Google style)

## Data Privacy & Compliance

### Personal Data Handling
- Personal ID numbers encrypted at rest
- Phone numbers hashed for lookups
- Device fingerprints anonymized
- Right to be forgotten implementation
- Data export functionality

### Audit Trail
- All voting actions logged
- Endorsement history tracked
- Leadership changes recorded
- SOS signals archived
- Arbitration cases documented

## Integration Points

### External Systems
- GeD database (membership verification)
- SMS gateway (phone verification)
- Electoral district mapping service
- Television/media integration (SOS escalation)

### Mobile App Integration
- RESTful API endpoints
- WebSocket support for real-time updates
- Push notification service
- Offline capability considerations

## Success Metrics

### Platform Health
- User registration rate
- Verification completion rate
- Active vs passive member ratio
- Endorsement success rate
- Ateuli formation rate

### Engagement Metrics
- Voting participation rate
- Initiative creation rate
- SOS signal volume and resolution rate
- Arbitration request volume
- Level progression rate

### System Performance
- API response times
- Error rates
- System uptime
- Database performance
- Cache hit rates
