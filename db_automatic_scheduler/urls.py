"""db_automatic_scheduler URL Configuration

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
from django.urls import path, include
from exam_scheduler import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from .routers import router
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'auth/', csrf_exempt(ObtainAuthToken.as_view())),
    path('', include('exam_scheduler.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset',),
    path('admin/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm',),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete',)

]
