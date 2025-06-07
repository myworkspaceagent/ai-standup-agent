from pydantic import BaseModel, EmailStr
from typing import Optional

class GoogleLoginRequest(BaseModel):
    google_email: EmailStr
    name: Optional[str]
    profile_pic: Optional[str]

class UserSetupRequest(BaseModel):
    google_email: EmailStr
    jira_email: Optional[EmailStr]
    jira_domain: Optional[str]
    jira_api_token: Optional[str]
    slack_email: Optional[EmailStr]
    timezone: Optional[str]
