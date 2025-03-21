"""untitled URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signin,name='signin'),
    path('sign_up',views.signup,name='signup'),
    path('score/',views.score,name='score'),
    path('ajlkgnkjvxiHKGS/',views.admin,name='admin'),
    path('ajlkgnkjvxiHKGS/table/',views.admin_table,name='admin_table'),
    path('api1/',views.api1,name='api1'),
    path('api2/',views.api2,name='api2'),
    path('api3/',views.api3,name='api3'),
    path('caipanflag/',views.api4,name='api4'),
]
