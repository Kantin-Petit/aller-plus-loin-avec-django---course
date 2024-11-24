from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
                                template_name='authentication/login.html',
                                redirect_authenticated_user=True), 
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
                                                        template_name='authentication/change-password.html',
                                                        success_url='/change-password-done/'), 
         name='change-password'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
                                                                 template_name='authentication/change_password_done.html'),
         name='change-password-done'),
    path('home/', blog.views.home, name='home'),
]
