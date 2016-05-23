from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from .models import Deal, Offer, Car
from .forms import RegisterCarForm, RegisterOfferForm

class IndexView(generic.ListView):
    model = Offer
    template_name = 'crms/index.html'
    context_object_name = 'Offerlist'

class OfferView(generic.DetailView):
    model = Offer
    template_name = 'crms/offer.html'

class DealView(generic.DetailView):
    model = Deal
    template_name = 'crms/deal.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'crms/user.html'
    context_object_name = "target_user"

# @login_required
class RegisterCarView(generic.edit.FormView):
    template_name = "crms/register_car.html"
    form_class = RegisterCarForm
    success_url = reverse_lazy('crms:index')

    def form_valid(self, form):
        print("-----form_valid begins------")
        form.user=self.request.user
        form.save()

        return super(RegisterCarView, self).form_valid(form)

class RegisterOfferView(generic.edit.FormView):
    template_name = "crms/register_offer.html"
    for_class = RegisterOfferForm
    success_url = reverse_lazy('crms:index')

    def form_valid(self, form):
        return super(RegisterOfferView, self).form_valid()

class RegisterDealView(generic.edit.FormView):
    pass
