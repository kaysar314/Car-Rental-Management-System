#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('crms:index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('crms:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('crms:index'))
