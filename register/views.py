"""
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.contrib.auth import login



class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')  # redirect after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # auto-login after register
        return response

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')  # Redirect after login
"""