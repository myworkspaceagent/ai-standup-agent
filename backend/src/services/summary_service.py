import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from integrations.google_auth import get_google_creds
from integrations.google_calendar import get_todays_meetings
from integrations.gmail import get_recent_emails
from utils.formatters import format_prompt

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)

def generate_daily_summary():
    creds = get_google_creds()
    calendar_events = get_todays_meetings(creds)
    emails = get_recent_emails(creds)

    prompt = format_prompt(calendar_events, emails)
    response = llm.invoke(prompt)

    return response.content
