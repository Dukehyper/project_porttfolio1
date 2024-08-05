# portfolio/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()

    projects = [
        {'title': 'Project 1', 'description': 'Description 1', 'behance_link': 'https://www.behance.net/'},
        {'title': 'Project 2', 'description': 'Description 2', 'behance_link': 'https://www.behance.net/'},
        {'title': 'Project 3', 'description': 'Description 3', 'behance_link': 'https://www.behance.net/'},
        {'title': 'Project 4', 'description': 'Description 4', 'behance_link': 'https://www.behance.net/'},
        {'title': 'Project 5', 'description': 'Description 5', 'behance_link': 'https://www.behance.net/'},
        {'title': 'Project 6', 'description': 'Description 6', 'behance_link': 'https://www.behance.net/'},
    ]

    context = {
        'form': form,
        'projects': projects,
    }
    return render(request, 'index.html', context)