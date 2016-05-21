#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'crms'
urlpatterns = [
    url(r'^$', views.DealView.as_view(), name='offer'),
]
