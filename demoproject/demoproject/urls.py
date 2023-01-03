"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from urlapp import views

urlpatterns = [
    # Function Based View
    # 1) http://127.0.0.1:8000/mysite
    # 2) http://127.0.0.1:8000/mysite/?username=raghu
    path('mysite/', views.my_view),
    # Named Query String
    # 1) http://127.0.0.1:8000/mysite/raghu
    path('mysite/<str:username>', views.view_named_query_sting),
    # Class Based View
    path('cbv/', views.MyView.as_view()),
]
