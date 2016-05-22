from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Deal, Offer, Car


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



class RegisterCarView():
    model = Car

class RegisterOfferView():
    model = Offer

class RegisterDealView():
    model = Deal
