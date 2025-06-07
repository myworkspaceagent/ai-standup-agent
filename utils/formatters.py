def format_prompt(events, emails):
    return f"""
You are a helpful assistant for a software engineer.

Here are today's inputs:

📅 Meetings:
{chr(10).join(['- ' + e for e in events])}

✉️ Emails:
{chr(10).join(['- ' + e for e in emails])}

Generate:
1. A **timesheet summary**
2. A **standup update** with:
  - ✅ What I did
  - 🚧 In progress
  - ❗ Blockers
"""