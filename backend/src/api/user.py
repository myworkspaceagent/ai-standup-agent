from fastapi import APIRouter
from db.models.user import UserSetupRequest
from services.user_service import update_handles

router = APIRouter()


@router.post("/user/setup")
def setup_user_handles(payload: UserSetupRequest):
    handles = {
        "jira_email": payload.jira_email,
        "jira_domain": payload.jira_domain,
        "jira_api_token": payload.jira_api_token,
        "slack_email": payload.slack_email,
        "timezone": payload.timezone
    }
    update_handles(payload.google_email, handles)
    return {"message": "User handles updated successfully."}
