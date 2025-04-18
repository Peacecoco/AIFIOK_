from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    return render(request, 'app/index.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def faq(request):
    return render(request, 'app/faq.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
               # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

               # Send email notification
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message}",
                'peeaacoco@gmail.com',  # Replace with your email
                ['abdullahivictor9@gmail.com'],  # Replace with the recipient's email
                fail_silently=False,
            )

            return redirect('success')  # Redirect to a success page or the same page
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})

def service(request):
    return render(request, 'app/service.html', {})

   # app/views.py
def success_view(request):
    return render(request, 'app/success.html')