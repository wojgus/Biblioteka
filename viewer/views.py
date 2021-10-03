from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, ListView
from viewer.forms import BookForm
from viewer.models import Book
from logging import getLogger

# Create your views here.
LOGGER = getLogger()

from django.contrib.auth.views import LoginView


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


def Test(request):
    a = request.GET.get('a')
    return render(
        request, template_name='base.html', context={

        }
    )


def Test1(request):
    b = request.GET.get('b')
    return render(
        request, template_name='index.html'
    )


class BookCreateView(FormView):
    template_name = 'form.html'
    form_class = BookForm


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
