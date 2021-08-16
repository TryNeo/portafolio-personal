from django.urls import path,register_converter
from ids_encoder import converters

from .views import *

register_converter(converters.HashidsConverter, 'hashids')


urlpatterns = [
    path('portfolio/detail/<hashids:pk>',PortfolioDetailView.as_view(),name='portfolio_details'),
    path('portfolio/',PortfolioView.as_view(), name='portfolio'),
    path('services/',ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/',AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),

]
