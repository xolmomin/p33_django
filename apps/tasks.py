from celery import shared_task

from django.core.mail import send_mail, EmailMessage
from django.db.models import Q
from django.template.loader import render_to_string

from apps.models import User
from root.settings import EMAIL_HOST_USER


@shared_task
def send_email(email: str):
    subject = 'Registration'
    context = {
        'app_name': 'P33 Group',
        'verification_url': 'https://localhost:8000/'
    }
    html_message = render_to_string('apps/auth/email_verification.html', context)
    mail = EmailMessage(subject, html_message, EMAIL_HOST_USER, [email])
    mail.send()

    return "Successfully sent email"


@shared_task
def send_all_user(msg):
    users_email = list(User.objects.exclude(Q(email='') | Q(email__isnull=True)).values_list('email', flat=True))
    subject = 'Registration'
    context = {
        'app_name': 'P33 Group',
        'verification_url': 'https://localhost:8000/'
    }
    html_message = render_to_string('apps/auth/email_verification.html', context)
    mail = EmailMessage(subject, html_message, EMAIL_HOST_USER, users_email)
    mail.send()

    return "Successfully sent email"
