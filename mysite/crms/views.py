from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Deal, Offer


class DealView(generic.ListView):
    model = Offer
    template_name = 'crms/offer.html'
    context_object_name = 'Offerlist'

