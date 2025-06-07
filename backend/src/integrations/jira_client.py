from jira import JIRA
import os

def get_jira_client():
    jira_server = os.getenv("JIRA_SERVER")
    email = os.getenv("JIRA_EMAIL")
    api_token = os.getenv("JIRA_API_TOKEN")

    options = {"server": jira_server}
    auth = (email, api_token)

    return JIRA(options=options, basic_auth=auth)
