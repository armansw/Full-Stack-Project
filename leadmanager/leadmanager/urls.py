from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('', include('accounts.urls')),
    # re_path('./../frontend/templates/frontend', TemplateView.as_view(template_name='index.html')),
]
