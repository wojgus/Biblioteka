from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, CreateView, DeleteView
from viewer.forms import BookForm
from viewer.models import Book
from logging import getLogger

# Create your views here.
LOGGER = getLogger()

from django.contrib.auth.views import LoginView, PasswordChangeView


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


def Test(request):
    a = request.GET.get('a')
    return render(
        request, template_name='base.html', context={

        }
    )


class RulesView(FormView):
    template_name = 'Rules.html'


def Rules(request):
    c = request.GET.get('c')
    return render(
        request, template_name='Rules.html', context={

        }
    )


def Test1(request):
    b = request.GET.get('b')
    return render(
        request, template_name='list_of_books.html', context={
            'books': Book.objects.all()
        }
    )


class BookCreateView(FormView):
    template_name = 'form.html'
    form_class = BookForm


class SearchResultsView(ListView):
    model = Book
    template_name = 'search.html'


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


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'AddEditBook.html'
    form_class = BookForm
    success_url = reverse_lazy('Book_create')

    def form_invalid(self, form):
        LOGGER.warning('zle dane w tworzeniu')
        return super().form_invalid(form)


class BookUpdateView(UpdateView):
    template_name = 'AddEditBook.html'
    form_class = BookForm
    model = Book

    def form_invalid(self, form):
        LOGGER.warning('złe dane w edycji')
        return super().form_invalid(form)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'DeleteBook.html'
    success_url = reverse_lazy('index')
    model = Book


class SearchResultsView(ListView):
    model = Book
    template_name = 'search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class SubmittablePasswordChangeForm(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')
