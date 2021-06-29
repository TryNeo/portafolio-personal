from django.urls import path
from .views.dashboard.views import DashboardView
from .views.contact.views import ContactView,ContactCreateView


urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/add', ContactCreateView.as_view(), name='contact_create'),
]
