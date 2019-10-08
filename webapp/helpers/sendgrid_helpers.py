from flask import render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from webapp.config import SENDGRID_API_KEY, FROM_EMAIL


def send_reg_email_to_user(email, password):
    subject = 'Ваши регистрационные данные в Doctor_CRM'
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject=subject,
        html_content=render_template('reg_email.html',
                                     email=email,
                                     password=password,
                                     ))
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception:
        pass
