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

]
