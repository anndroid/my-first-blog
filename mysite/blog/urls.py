# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:22:38 2016

@author: magda
"""

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]