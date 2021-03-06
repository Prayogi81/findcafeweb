"""findcafeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from findcafe.views import list_cafe,tambah_cafe, edit_cafe
from findcafe.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cafe', CafeViewset)

urlpatterns = [
    path('', include('findcafe.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('list-cafe/', list_cafe),
    path('tambah-cafe/', tambah_cafe),
    path('list-cafe/edit-cafe/<int:id_cafe>', edit_cafe, name='edit_cafe'),
]
