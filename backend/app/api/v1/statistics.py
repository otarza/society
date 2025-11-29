from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()

@router.get("/platform")
async def read_platform_stats(
    db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Get global platform statistics.
    """
    # TODO: Implement logic
    return {"users": 0}
