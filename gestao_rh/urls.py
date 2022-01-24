from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth import  views as auth_views
import django
from django.contrib.auth import urls

urlpatterns = [
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls') ),
    path('admin/', admin.site.urls),
    path('accounts/', include( django.contrib.auth.urls ) )
]
