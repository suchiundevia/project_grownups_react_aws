"""hints-project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
# Directly imported views and mapped the url
from accounts import views as account_views
# Media roots for development phase of project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Profile Page
    path('profile/', account_views.profile, name='profile'),
    # Sign Up Page
    path('signup/', account_views.signup, name='signup'),
    # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Logout Page
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # Reset Password Page (Specify Email)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    # Reset Password Page (Delivery Message + Email)
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    # Reset Password Page (Reset Password - Enter New Password)
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # Reset Password (Final Confirmation Message and Redirection Link to Login Page)
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    # Home Page
    path('', include('activity.urls')),
    # Admin Panel
    path('admin/', admin.site.urls),
]
# URL pattern for media files during development phase.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
