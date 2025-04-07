"""
URL configuration for mysite project.

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
from mysite import views

urlpatterns = [
    path('my-admin/', admin.site.urls),
    path("about-us/", views.aboutUs, name="about"),
    path("courses/", views.course),
    path("courses/<courseId>", views.CourseById),
    path("", views.homePage, name="home"),
    path("contact-us/", views.contact, name="contact"),
    path("userform/", views.userForm),
    path("submitform/", views.submitform, name="submitform")
]
