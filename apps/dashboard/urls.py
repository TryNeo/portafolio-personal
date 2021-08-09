from django.urls import path
from .views.dashboard.views import DashboardView
from .views.contact.views import *
from .views.social_media.views import *
from .views.service.views import *
urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    #Urls Contact
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/add', ContactCreateView.as_view(), name='contact_create'),
    path('contact/edit/<int:pk>', ContactUpdateView.as_view(), name='contact_update'),
    path('contact/delete/<int:pk>', ContactDeleteView.as_view(), name='contact_delete'),
    
    #Urls Social Media
    path('social-media/',SocialMediaView.as_view(),name='social_media'),
    path('social-media/json', SocialMediaListView.as_view(), name='social_media_json'),
    path('social-media/add', SocialMediaCreateView.as_view(), name='social_media_create'),
    path('social-media/edit/<int:pk>', SocialMediaUpdateView.as_view(), name='social_media_edit'),
    path('social-media/delete/<int:pk>', SocialMediaDeleteView.as_view(), name='social_media_delete'),

    #Urls Service
    path('service/',ServiceView.as_view(), name='service'),
    path('service/json',ServiceListView.as_view(), name='service_json'),
    path('service/add', ServiceCreateView.as_view(), name='service_create'),
    path('service/edit/<int:pk>', ServiceUpdateView.as_view(), name='service_edit'),
    path('service/delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),
]
