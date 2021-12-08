# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(send_from: str, send_to: str, subject: str, body: str, api_key: str):
    message = Mail(
        from_email=send_from,
        to_emails=send_to,
        subject=subject,
        html_content=body)
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
