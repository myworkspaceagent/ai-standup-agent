from google_auth_oauthlib.flow import InstalledAppFlow
import os
from dotenv import load_dotenv

load_dotenv()

scopes = os.getenv("GOOGLE_API_SCOPES").split(",")
creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")

flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
creds = flow.run_local_server(port=0)

print("Access Token:", creds.token)
