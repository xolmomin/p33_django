from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

from root.settings import EMAIL_HOST_USER


def send_email(email: str):
    subject = 'Registration'
    context = {
        'app_name': 'P33 Group',
        'verification_url': 'https://localhost:8000/'
    }
    html_message = render_to_string('apps/auth/email_verification.html', context)
    mail = EmailMessage(subject, html_message, EMAIL_HOST_USER, [email])
    mail.send()
