# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# Further customising the sign up form to add email
class UserSignUpForm(UserCreationForm):
    # Email required
    email = forms.EmailField()

    # Specifying the model which is interacting with the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Model Form - form that works with a specific database model
# Update user details (only username and email address)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Specifying the model which is interacting with the form
    class Meta:
        model = User
        fields = ['username', 'email']


# To update user profile, another form must be created
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
