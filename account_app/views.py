from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# LoginRequiredMixin: Prevent a user from adding an activity if they have not yet logged in (rather than decorator)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


# FUNCTION BASED VIEWS
def signup(request):
    # Check if the request is valid
    if request.method == 'POST':
        # Get the request
        form = UserSignUpForm(request.POST)
        # Check if the data entered in the form is valid
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # Display success message
            messages.success(request, f'Welcome! Your account has been created! You now should be able to login.')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})


# A user must be logged in to view the profile page (decorator prevents access to this page if user is not logged in)
@login_required
def profile(request):
    # Check if the request is valid and add fields so the user can update their information
    if request.method == 'POST':
        # Instantiate the forms
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)
        user_profile_form = UserProfileUpdateForm(request.POST,
                                                  request.FILES,
                                                  instance=request.user.userprofile)
        # Check if the data entered in the form is valid
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            # Display success message
            messages.success(request, f'Your details have been updated.')
            # To prevent the browser asking confirmation on reload
            # Because of previously entered data
            # The GET request sent again when the page is redirected prevents this
            return redirect('profile')

    else:
        # Instantiate the forms
        user_form = UserUpdateForm(instance=request.user)
        user_profile_form = UserProfileUpdateForm(instance=request.user.userprofile)
    # Pass to template
    context = {'user_form': user_form,
               'user_profile_form': user_profile_form}
    return render(request, 'profile.html', context)


# A user must be logged in to view the profile page (decorator prevents access to this page if user is not logged in)
# Delete an account
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    # On deletion - redirect to home page
    success_url = '/'
    # Typical path for a class based list view <app>/<model>_<viewType>.html
    template_name = 'account_app/user_delete.html'
