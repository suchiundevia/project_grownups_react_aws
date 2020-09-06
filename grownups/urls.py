from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
# Directly imported views and mapped the url
from account_app import views as account_views
# Media roots for development phase of project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Google and Social Media Login
    path('accounts/', include('allauth.urls')),
    # Profile Page
    path('profile/', account_views.profile, name='profile'),
    # Sign Up Page
    path('signup/', account_views.signup, name='signup'),
    # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='account_app/login.html'), name='login'),
    # Logout Page
    path('logout/', auth_views.LogoutView.as_view(template_name='account_app/logout.html'), name='logout'),
    # Reset Password Page (Specify Email)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account_app/password_reset.html'),
         name='password_reset'),
    # Reset Password Page (Delivery Message + Email)
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account_app/password_reset_done.html'),
         name='password_reset_done'),
    # Reset Password Page (Reset Password - Enter New Password)
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # Reset Password (Final Confirmation Message and Redirection Link to Login Page)
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account_app/password_reset_complete.html'),
         name='password_reset_complete'),
    # Home Page
    path('', include('base_app.urls')),
    # Admin Panel
    path('admin/', admin.site.urls),
]
# URL pattern for media files during development phase.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
