#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'crms'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/offer/$', views.OfferView.as_view(), name='offer'),
    url(r'^(?P<pk>[0-9]+)/deal/$', views.DealView.as_view(), name='deal'),
    url(r'^(?P<pk>[0-9]+)/user/$', views.UserView.as_view(), name='user'),
    url(r'^register_car/$', views.RegisterCarView.as_view(), name='register_car'),
    url(r'register_offer/$', views.RegisterOfferView.as_view(), name='register_offer')
]
