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
    # compatibility route (older links)
    path('investment/', views.investments, name='investment'),
    path('companies/developments/', views.developments, name='developments'),
    path('companies/tasty/', views.tasty, name='tasty'),
    path('companies/transport/', views.transport, name='transport'),
    path('companies/workshop/', views.workshop, name='workshop'),
    path('companies/ekhaya/', views.ekhaya, name='ekhaya'),
    path('companies/nitro/', views.nitro_group, name='nitro_group'),
    path('ibr_africa/', views.ibr_africa, name='ibr_africa'),
    path('ibr_foundation/', views.ibr_foundation, name='ibr_foundation'),
    path('ibr_holdings/', views.ibr_holdings, name='ibr_holdings'),


]
