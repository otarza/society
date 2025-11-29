from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core import security
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/send-verification-code")
async def send_verification_code(
    phone_number: str,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Send SMS verification code to phone number.
    """
    # TODO: Implement SMS gateway integration
    return {"message": "Verification code sent"}

@router.post("/verify-phone")
async def verify_phone(
    phone_number: str,
    code: str,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Verify phone number with code and return JWT tokens.
    """
    # TODO: Validate code
    # TODO: Create or update user
    # TODO: Generate tokens
    return {
        "access_token": "token",
        "refresh_token": "refresh_token",
        "token_type": "bearer"
    }

@router.post("/refresh")
async def refresh_token(
    refresh_token: str,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Refresh access token using refresh token.
    """
    # TODO: Validate refresh token
    # TODO: Generate new access token
    return {
        "access_token": "new_token",
        "token_type": "bearer"
    }

@router.post("/logout")
async def logout(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Logout user (invalidate refresh token).
    """
    # TODO: Invalidate refresh token
    return {"message": "Logged out successfully"}
