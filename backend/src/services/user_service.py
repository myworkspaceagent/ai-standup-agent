from db.repositories.user_repository import (
    upsert_user_by_google_email,
    update_user_handles,
    get_user_by_google_email
)

def register_or_login_user(google_email, name=None, picture=None):
    upsert_user_by_google_email(google_email, name, picture)

def update_handles(google_email, handles: dict):
    update_user_handles(google_email, handles)

def fetch_user(google_email):
    return get_user_by_google_email(google_email)
