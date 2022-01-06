from django.urls import path
from master.views import HomeView, CalculateView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
path('calculate/', CalculateView.as_view(), name='calculate'),
]