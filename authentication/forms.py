"""
authentication forms
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm
from .models import User
from django import forms
import re
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


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




# edits
class EditFirstName(forms.Form):
    first_name = forms.CharField(max_length=255)

    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data['first_name']
        first_name_regex = re.compile(r"^[A-Za-z]{2,255}$")
        if not first_name_regex.match(first_name):
            raise forms.ValidationError("Name contains invalid characters")
        else:
            if len(first_name) < 2:
                raise forms.ValidationError("Name is too short")
            else:
                if len(first_name) > 255:
                    raise forms.ValidationError("Name is too long")
        return first_name


class EditLastName(forms.Form):
    last_name = forms.CharField(max_length=255)

    def clean_first_name(self, *args, **kwargs):
        last_name = self.cleaned_data['first_name']
        last_name_regex = re.compile(r"^[A-Za-z]{2,255}$")
        if not last_name_regex.match(last_name):
            raise forms.ValidationError("Name contains invalid characters")
        else:
            if len(last_name) < 2:
                raise forms.ValidationError("Name is too short")
            else:
                if len(last_name) > 255:
                    raise forms.ValidationError("Name is too long")
        return last_name


class EditEmailForm(forms.Form):
    email = forms.CharField(max_length=2089, widget=forms.EmailInput(attrs={'id': 'email',"placeholder":"Enter your new email"}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data['email']
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError:
            raise forms.ValidationError("you entered invalid email!!")
        user_with_email = User.objects.filter(email=email)
        if user_with_email:
            raise forms.ValidationError("{}{}".format(email, " is already associated with another account"))
        return email


class EditPassword(forms.Form):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'id': 'password', 'name': 'password'}))
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'id': 'con-password',
                                                                                         'name': 'con-password'}))

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data['password']
        password_regex = re.compile(r"^[\w#@$?!]+$")
        if len(password) < 5:
            raise forms.ValidationError("Password is too short")
        else:
            if len(password) > 50:
                raise forms.ValidationError("Password is too long maximum of 50 characters is allowed")
            else:
                if not password_regex.match(password):
                    raise forms.ValidationError("Password contains invalid symbols allowed symbols are #@$?!*")
        return password

    def clean_confirm_password(self, *args, **kwargs):
        confirm_password = self.cleaned_data['confirm_password']
        try:
            password = self.cleaned_data['password']
        except KeyError:
            password = ''
        if password:
            if not password == confirm_password:
                raise forms.ValidationError("Passwords do not match")
        return confirm_password
