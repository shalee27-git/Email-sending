from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to Our Platform!"
    message = "Thank you for signing up!"
    sender = "srishyam4@gmail.com"

    send_mail(subject, message, sender, [user_email])
    return f"Email sent to {user_email}"