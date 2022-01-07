from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"


class CalculateView(TemplateView):
    template_name = "calc.html"


class CatalanView(TemplateView):
    template_name = "calc_catalan.html"