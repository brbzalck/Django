from django.urls import path
from . import views

# HTPP Resquest <-> HTTP Response

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]
