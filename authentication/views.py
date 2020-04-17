"""
views for authentication
"""

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import RegistrationForm
from .models import User
from .forms import EditEmailForm


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



class ProfileView(generic.DetailView):
    model=User
    template_name="registration/profile.html"
    context_object_name="user"



def edit_email_view(request):
    if request.method == "GET":
        form = EditEmailForm()
        return render(request, 'profile_editing/edit_email.html', {"form":form})

    elif request.method == "POST":
        form = EditEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['email']
            user = User.objects.get(email=request.user.email)
            user.email = new_email
            user.save()
            return redirect(reverse("profile", args=(request.user.id,)))
        return render(request, "profile_editing/edit_email.html", {"form":form})