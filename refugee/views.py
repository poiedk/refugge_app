from django.shortcuts import render
from django.views.generic import CreateView
from .models import refugge



class refugeeCreateView(CreateView):
    model = refugge
    fields = '__all__'
    template_name = "pages/refugee_create.html"
