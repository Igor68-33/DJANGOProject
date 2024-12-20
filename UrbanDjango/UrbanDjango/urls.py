"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from task2 import views
# from task3 import views
# from task4 import views
from task5 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('func', views.func_view, name='func'),
    # path('class', views.class_view.as_view(), name='class'),
    # path('', views.home, name='home'),
    # path('shop', views.shop, name='shop'),
    # path('basket', views.basket, name='basket'),
    # path('menu', views.menu, name='menu'),
    path('', views.sign_up_by_html, name='func'),
    path('django_sign_up', views.sign_up_by_django, name='func'),
]
