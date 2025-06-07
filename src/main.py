import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from integrations.google_calendar import get_todays_meetings
from scripts.test_google_auth import get_google_creds
from integrations.gmail import get_recent_emails
from utils.formatters import format_prompt

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)

# Load creds
creds = get_google_creds()

# Fetch Data
calendar_events = get_todays_meetings(creds)
emails = get_recent_emails(creds)

# Format Prompt
prompt = format_prompt(calendar_events, emails)

# Run Gemini
response = llm.invoke(prompt)

print("\n=== Gemini Output ===\n")
print(response.content)