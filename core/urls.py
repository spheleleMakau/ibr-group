from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('companies/', views.companies, name='companies'),
    path('foundation/', views.foundation, name='foundation'),
    path('contact/', views.contact, name='contact'),
    path('companies/agriculture/', views.agriculture, name='agriculture'),
    path('companies/mining/', views.mining, name='mining'),
    path('companies/retail/', views.retail, name='retail'),
    path('companies/investments/', views.investments, name='investments'),
    path('companies/developments/', views.developments, name='developments'),
    path('companies/tasty/', views.tasty, name='tasty'),
    path('companies/transport/', views.transport, name='transport'),
    path('companies/workshop/', views.workshop, name='workshop'),
    path('companies/ekhaya/', views.ekhaya, name='ekhaya'),
]
