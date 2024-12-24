
from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

from .gmail_utility import authenticate_gmail, create_message, create_draft, send_mail
from agentops import record_tool

import os

class GmailToolInput(BaseModel):
    """Input schema for GmailTool."""

    body: str = Field(..., description="The body of the email to send.")

@record_tool("This is used for gmail draft emails.")
class GmailTool(BaseTool):
    name: str = "GmailTool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:
        try:
            service = authenticate_gmail()

            sender = os.getenv("GMAIL_SENDER")
            to = os.getenv("GMAIL_RECIPIENT")
            subject = "요약"
            message_text = body

            message = create_message(sender, to, subject, message_text)
            sent_message = send_mail(service, "me", message)
            if sent_message:
                return f"Email sent successfully! Message Id: {sent_message['id']}"
            return "Failed to send email"
        except Exception as e:
            return f"Error sending email: {e}"
