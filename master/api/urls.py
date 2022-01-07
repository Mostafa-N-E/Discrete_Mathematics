from django.urls import path, include

from . import views

urlpatterns = [
    path('calculate/', views.CalculateApi.as_view(), name='calculate_api'),
    path('contact_us/',views.Contact_us.as_view(), name='contact_us'),
    path('catalan/', views.CatalanApi.as_view(), name='catalan_api'),
]