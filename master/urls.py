from django.urls import path
from master.views import HomeView, CalculateView, CatalanView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('calculate/', CalculateView.as_view(), name='calculate'),
    path('catalan/', CatalanView.as_view(), name='catalan'),
]