"""Project URL Configuration

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
from django.urls import path

from main.views import index
from main.views import blog, article
from main.views import download
from main.views import contact

from main.views import en_index
from main.views import en_blog, en_article
from main.views import en_download
from main.views import en_contact


urlpatterns = [
    path('', index, name="index"),
    path('blog', blog, name='blog'),
    path('aticle', article, name='article'),
    path('download', download, name='download'),
    path('contact', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('<slug:url>', article, name='article'),

    # ENGLISH VERSION
    path('en/', en_index, name="en_index"),
    path('en/blog', en_blog, name='en_blog'),
    path('en/aticle', en_article, name='en_article'),
    path('en/download', en_download, name='en_download'),
    path('en/contact', en_contact, name='en_contact'),
    path('en/<slug:url>', en_article, name='en_article'),
]


