from fastapi import APIRouter

from app.api.v1 import (
    auth,
    users,
    territories,
    ateulis,
    endorsements,
    elections,
    sos,
    initiatives,
    arbitration,
    hierarchy,
    gamification,
    notifications,
    statistics
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(territories.router, prefix="/territories", tags=["territories"])
api_router.include_router(ateulis.router, prefix="/ateulis", tags=["ateulis"])
api_router.include_router(endorsements.router, prefix="/endorsements", tags=["endorsements"])
api_router.include_router(elections.router, prefix="/elections", tags=["elections"])
api_router.include_router(sos.router, prefix="/sos", tags=["sos"])
api_router.include_router(initiatives.router, prefix="/initiatives", tags=["initiatives"])
api_router.include_router(arbitration.router, prefix="/arbitration", tags=["arbitration"])
api_router.include_router(hierarchy.router, prefix="/hierarchy", tags=["hierarchy"])
api_router.include_router(gamification.router, prefix="/gamification", tags=["gamification"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(statistics.router, prefix="/statistics", tags=["statistics"])
