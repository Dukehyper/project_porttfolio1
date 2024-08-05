# portfolio/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact, Project

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()


    context = {
        'form': form,
        'projects' : Project.objects.all()
	}

   
    return render(request, 'index.html', context)