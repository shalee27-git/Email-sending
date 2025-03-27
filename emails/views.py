from django.shortcuts import render
from .tasks import send_welcome_email

def register_user(request):
    if request.method == "POST":
        email = request.POST['email']
        send_welcome_email.delay(email)
        return render(request, 'registration_success.html')
    return render(request, 'register.html')


