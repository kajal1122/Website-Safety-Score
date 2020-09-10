from django.urls import include, path
from .views import SiteView, SiteSearchAPIView
from rest_framework import routers



urlpatterns = [
    path('',SiteView.as_view()),
    path('search',SiteSearchAPIView.as_view())
]
