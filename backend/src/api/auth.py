from fastapi import APIRouter
from db.models.user import GoogleLoginRequest
from services.user_service import register_or_login_user

router = APIRouter()

@router.post("/auth/google")
def login_or_register(payload: GoogleLoginRequest):
    register_or_login_user(
        google_email=payload.google_email,
        name=payload.name,
        picture=payload.profile_pic
    )
    return {"message": "User logged in or registered successfully."}
