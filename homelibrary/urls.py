"""homelibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from p_library import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from allauth.account.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index,  name='index'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redactions/', views.redactions),
    path('books/', views.books),
    path('authors/', views.authors),
    path('renters/', views.books_rent),
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    url(r'^accounts/', include('allauth.urls')),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

