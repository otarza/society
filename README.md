# Girchi Digital Polis - Backend API Documentation

## Project Overview

This repository contains comprehensive documentation and planning for the **Girchi Digital Polis** backend API - a society management platform enabling decentralized self-governance through a hierarchical representative system.

## 📚 Documentation Structure

### Core Documentation

1. **[Technical Requirements](./docs/technical-requirements.md)**
   - Functional requirements (FR-1 through FR-10)
   - Non-functional requirements (security, performance, scalability)
   - Technology stack decisions
   - Success metrics

2. **[Data Model & Database Schema](./docs/data-model.md)**
   - Entity Relationship Diagram (ERD)
   - 19 database tables with complete specifications
   - Relationships and constraints
   - Security and performance considerations
   - Enumeration types

3. **[API Architecture](./docs/api-architecture.md)**
   - 80+ RESTful API endpoints
   - Authentication & authorization flows
   - Request/response schemas
   - WebSocket events for real-time updates
   - Error codes and rate limiting
   - Security best practices

4. **[System Architecture](./docs/system-architecture.md)**
   - Architecture diagrams
   - Component descriptions
   - Data flow examples
   - Security architecture
   - Scalability strategy
   - Monitoring & observability
   - Deployment architecture

### Initial Concept

- **[initial.md](./initial.md)** - Original concept document (Georgian)

## 🎯 Key Features

### User Management
- Three user roles: Unverified, GeDer (verified members), Supporters
- Two status levels: Passive and Active members
- Phone verification and GeD database integration
- Device fingerprinting for fraud prevention

### Hierarchical Organization
- **Ateuli** (10 members) → **Ormotsdaateuli** (50) → **Aseuli** (100) → **Ataseuli** (1000)
- Territory-based automatic organization
- Elected leadership at each level
- Satatbiro (Council) composed of all Atasistavis

### Endorsement System
- GeDers can endorse supporters (Tavdebi system)
- Endorsement limits per GeDer (5-10 people)
- Accountability through penalty system
- Self-regulating network

### Elections & Voting
- Direct voting for Atistavi (leader of 10)
- Hierarchical elections for higher levels
- Parliamentary list voting
- Secure vote tracking with verification hashes

### SOS System
- Emergency signal creation
- Moral filter verification
- Hierarchical escalation
- Media integration for critical cases

### Initiatives & Petitions
- Community-driven initiatives
- Support threshold tracking
- Automatic assignment to representatives
- Category-based organization

### Arbitration
- Dispute resolution system
- Representative-led arbitration
- Case tracking and history

### Gamification
- Visual progress indicators
- Level-based capability unlocking
- Motivation cycle for growth
- Achievement system

## 🏗️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL 15+** - Primary database with PostGIS
- **SQLAlchemy 2.0** - ORM with async support
- **Alembic** - Database migrations
- **Redis** - Caching and session management
- **Celery** - Background task processing
- **JWT** - Authentication

### DevOps
- **Docker & Docker Compose** - Containerization
- **Kubernetes** - Production orchestration
- **Prometheus & Grafana** - Monitoring
- **ELK Stack** - Logging

## 📊 Database Schema

The system uses 19 core tables:

1. **users** - Central user entity
2. **ged_verifications** - GeD membership verification
3. **device_fingerprints** - Device tracking
4. **endorsements** - Tavdebi relationships
5. **territories** - Electoral districts
6. **ateulis** - Groups of 10
7. **ormotsdaateulis** - Groups of 50
8. **aseulis** - Groups of 100
9. **ataseulis** - Groups of 1000
10. **elections** - Election management
11. **election_candidates** - Candidate registration
12. **votes** - Vote records
13. **sos_signals** - Emergency signals
14. **sos_escalations** - Signal escalation tracking
15. **initiatives** - Community initiatives
16. **initiative_supports** - Initiative support tracking
17. **arbitration_cases** - Dispute resolution
18. **audit_logs** - Comprehensive audit trail
19. **notifications** - User notifications

## 🔐 Security Features

- **Authentication**: JWT with refresh token rotation
- **Encryption**: AES-256 for sensitive data (personal IDs, phone numbers)
- **Hashing**: Bcrypt for passwords, SHA-256 for device fingerprints
- **Authorization**: Role-based access control (RBAC)
- **Audit Logging**: Comprehensive tracking of all critical actions
- **Rate Limiting**: Protection against abuse
- **HTTPS Only**: Enforced in production

## 📈 Scalability

- **Horizontal Scaling**: Stateless API instances
- **Database Replication**: Read replicas for queries
- **Caching Strategy**: Multi-level caching with Redis
- **Background Jobs**: Distributed task processing
- **Load Balancing**: nginx for traffic distribution

## 🚀 Next Steps

### For Development Team

1. **Review Documentation**
   - Read all documentation files in `/docs`
   - Understand data model and relationships
   - Review API endpoint specifications

2. **Environment Setup**
   - Set up local development environment
   - Configure external service credentials (SMS, GeD database)
   - Set up monitoring and logging

3. **Implementation Priorities**
   - Phase 1: Authentication & User Management
   - Phase 2: Territory & Group Management
   - Phase 3: Endorsement System
   - Phase 4: Elections & Voting
   - Phase 5: SOS, Initiatives, Arbitration
   - Phase 6: Gamification & Analytics

4. **External Integrations**
   - GeD database API integration
   - SMS gateway (Twilio, etc.)
   - Push notification service
   - Electoral district mapping service

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.11+

### Quick Start

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Start services**
   ```bash
   cp .env.example .env
   docker-compose up -d
   ```

3. **Run migrations**
   ```bash
   docker-compose exec app alembic upgrade head
   ```

4. **Access API**
   - Documentation: http://localhost:8000/api/v1/docs
   - Database UI: http://localhost:8080

For detailed development instructions, see [docs/DEVELOPMENT.md](backend/docs/DEVELOPMENT.md).

## 🎓 Learning Path

Are you new to this technology stack? We have prepared a comprehensive guide to help you get started.

👉 **[Start the Junior Developer Learning Path](backend/docs/LEARNING_PATH.md)**

This guide covers:
- **The Big Picture**: Understanding the business logic and data model
- **The Environment**: Mastering Docker and local setup
- **Modern Python**: Type hints, Pydantic, and Async
- **The Database**: SQLAlchemy ORM and Migrations
- **The API**: FastAPI and Dependency Injection

Each module includes practical exercises to build your skills.

## 📝 API Endpoints Summary

### Authentication (4 endpoints)
- Phone verification and login
- Token refresh
- Logout

### Users (5 endpoints)
- Profile management
- Onboarding
- User search

### Territories (5 endpoints)
- Territory listing and search
- Statistics

### Groups (7 endpoints)
- Ateuli creation and management
- Member management

### Endorsements (7 endpoints)
- Request and approval workflow
- Supporter management

### Elections (7 endpoints)
- Election management
- Candidate registration
- Voting
- Results

### SOS System (7 endpoints)
- Signal creation
- Verification
- Escalation

### Initiatives (8 endpoints)
- Initiative creation
- Support management
- Assignment

### Arbitration (6 endpoints)
- Case management
- Resolution

### Hierarchy (6 endpoints)
- Overview and statistics
- Position tracking

### Gamification (4 endpoints)
- Progress tracking
- Achievements
- Leaderboard

### Notifications (4 endpoints)
- Notification management

### Statistics (4 endpoints)
- Platform analytics

**Total: 80+ API endpoints**

## 🎓 Development Workflow

1. **Git Workflow**: Feature branches → Develop → Main
2. **CI/CD**: Automated testing and deployment
3. **Code Quality**: 80% test coverage minimum
4. **Documentation**: Comprehensive API docs (Swagger/ReDoc)
5. **Code Review**: Required for all PRs

## 📞 Support & Contact

For questions about this documentation or the project:
- Review the detailed documentation in `/docs`
- Check the implementation plan for development guidance
- Refer to API architecture for endpoint specifications

## 📄 License

[To be determined]

---

**Version**: 1.0  
**Last Updated**: 2025-11-28  
**Status**: Planning Complete - Ready for Implementation
