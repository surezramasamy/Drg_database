from django.shortcuts import render
from django.views.generic import ListView
from .models import Item_Detail

class HomePageView(ListView):
    model = Item_Detail
    template_name = 'home.html'
