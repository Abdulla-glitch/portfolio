from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    success = False
    skills = ["HTML", "CSS", "JavaScript", "Python", "Flask", "Django", "SQL", "Git"]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        try:
            send_mail(subject, body, from_email, to_email)
            success = True
        except Exception as e:
            print("Error sending email:", e)

    return render(request, 'myapp/index.html', {'success': success, 'skills': skills})


