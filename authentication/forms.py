"""
authentication forms
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form
    """
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form
    """
    class Meta:
        model = User
        fields = ('email',)



class RegistrationForm(CustomUserCreationForm):
    """
    registrations form
    """

    class Meta:
        model = User
        fields = ("email", "password1", "password2", )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EmailValidationOnForgotPassword(PasswordResetForm):
    """
    form to validate if email exits before sending reset password link
    """
    def clean_email(self):
        """
        function to clean email addess
        """
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified Email address."
            self.add_error('email', msg)
        return email