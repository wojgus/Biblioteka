"""biblioteka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import viewer
from viewer.models import Genre, Book
from viewer.views import Test, SubmittableLoginView, Test1, BookCreateView, BookUpdateView, BookDeleteView, \
    SearchResultsView, RulesView, Rules

admin.site.register(Book)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Test),
    path('login', SubmittableLoginView.as_view(), name='login'),
    path('register', viewer.views.register, name='register'),
    # path('index', Test1),
    path('create', BookCreateView.as_view(), name='add_book'),
    path('update/<pk>', BookUpdateView.as_view(), name='update_book'),
    path('list', Test1, name='list_of_books'),
    path('delete/<pk>', BookDeleteView.as_view(), name='delete'),
    path('search',SearchResultsView.as_view(), name='search'),
    path('rules',Rules, name='rules'),

]
