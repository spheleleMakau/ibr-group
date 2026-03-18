from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('companies/', views.companies, name='companies'),
    path('foundation/', views.foundation, name='foundation'),
    path('contact/', views.contact, name='contact'),
]
