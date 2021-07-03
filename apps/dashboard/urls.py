from django.urls import path
from .views.dashboard.views import DashboardView
from .views.contact.views import ContactView,ContactCreateView,ContactUpdateView,ContactDeleteView
from .views.social_media.views import SocialMediaView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    #Urls Contact
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/add', ContactCreateView.as_view(), name='contact_create'),
    path('contact/edit/<int:pk>', ContactUpdateView.as_view(), name='contact_update'),
    path('contact/delete/<int:pk>', ContactDeleteView.as_view(), name='contact_delete'),
    #Urls Social Media
    path('social/', SocialMediaView.as_view(), name='social_media'),
]
