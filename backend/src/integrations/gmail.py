from googleapiclient.discovery import build

def get_recent_emails(creds, max_results=5):
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])

    email_subjects = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
        headers = msg_data.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        email_subjects.append(subject)

    return email_subjects
