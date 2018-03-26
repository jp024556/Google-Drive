"""Google_Drive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from gdriveApp import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index,name='Default Page'),
    re_path(r'register/', views.register,name='Registeration Page'),
    re_path(r'login/', views.login,name='Login Page'),
    re_path(r'upload/', views.upload,name='Upload Page'),
    re_path(r'logout/', views.log_out,name='Log Out'),
    re_path(r'myUploads/', views.myUploads,name='myUploads'),
    re_path(r'about/', views.aboutUs,name='AboutUs'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
