from django.urls import path
from .views.dashboard.views import DashboardView
from .views.contact.views import *
from .views.social_media.views import *
from .views.service.views import *
from .views.category.views import *
from .views.portfolio.views import *
from .views.client.views import *
from .views.testimonial.views import *

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

    #Urls Category
    path('category/',CategoryView.as_view(), name='category'),
    path('category/json',CategoryListView.as_view(), name='category_json'),
    path('category/add', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    #Urls Portfolio
    path('portfolio/',PortfolioView.as_view(), name='portfolio'),
    path('portfolio/json',PortfolioListView.as_view(), name='portfolio_json'),
    path('portfolio/add', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolio/edit/<int:pk>', PortfolioUpdateView.as_view(), name='portfolio_edit'),
    path('portfolio/delete/<int:pk>', PortfolioDeleteView.as_view(), name='portfolio_delete'),

    #Urls Client
    path('client/',ClientView.as_view(), name='client'),
    path('client/json',ClientListView.as_view(), name='client_json'),
    path('client/add', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    #Urls Testimonial
    path('testimonial/',TestimonialView.as_view(), name='testimonial'),
    path('testimonial/json',TestimonialListView.as_view(), name='testimonial_json'),
    path('testimonial/add', TestimonialCreateView.as_view(), name='testimonial_create'),
    path('testimonial/edit/<int:pk>', TestimonialUpdateView.as_view(), name='testimonial_edit'),
    path('testimonial/delete/<int:pk>', TestimonialDeleteView.as_view(), name='testimonial_delete'),
]
