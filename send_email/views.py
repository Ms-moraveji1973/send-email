from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage

from .forms import  EmailForms

# Create your views here.
def home_page(request):
    if request.method == 'GET':
        form = EmailForms()
        return render(request , "emails/home.html" ,{'form':form})
    if request.method == "POST":
        form = EmailForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            email_message = EmailMessage(
                subject=subject,
                body=content,
                to=[email]
            )
            email_message.send()

            return HttpResponse("Your request has been sent")
        else:
            return HttpResponse("Your request was not valid")

