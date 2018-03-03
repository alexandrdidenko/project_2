# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from home_page.models import *


# Create your views here.
def index_view(request):
    return render(request, 'home_page/index.html', locals())
