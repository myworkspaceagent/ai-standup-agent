from db.mongo_client import users_collection

def upsert_user_by_google_email(google_email, name=None, picture=None):
    query = {"google_email": google_email}
    update = {
        "$set": {
            "google_email": google_email,
            "name": name,
            "profile_pic": picture
        }
    }
    users_collection.update_one(query, update, upsert=True)

def update_user_handles(google_email, handles: dict):
    query = {"google_email": google_email}
    update = {"$set": handles}
    users_collection.update_one(query, update)

def get_user_by_google_email(google_email):
    return users_collection.find_one({"google_email": google_email})