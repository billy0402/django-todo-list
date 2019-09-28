"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import root
from users.views import register

urlpatterns = [
    path('', root, name='root'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             subject_template_name='users/password_reset_subject.txt',
             email_template_name='users/password_reset_email.html',
             html_email_template_name='users/password_reset_html_email.html',
             success_url='/todos/'
         ),
         name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             post_reset_login=True,
             success_url='/todos/'
         ),
         name='password_reset_confirm'),

    path('tutorial/', include('tutorial.urls')),
    path('posts/', include('posts.urls')),
    path('todos/', include('todos.urls')),
    path('api/', include('api.urls')),

    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
