from datetime import datetime, timedelta
from googleapiclient.discovery import build


def get_todays_meetings(creds):
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"
    end = (datetime.utcnow() + timedelta(days=1)).isoformat() + "Z"

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        timeMax=end,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return [e.get('summary', 'No Title') for e in events]
