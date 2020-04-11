"""
views for authentication
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

def register(request):
    """
    view to handle users registration
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('authentication:register')
    else:
        form = RegistrationForm()

    context = {'form':form}

    return render(request, 'registration/register.html', context=context)
