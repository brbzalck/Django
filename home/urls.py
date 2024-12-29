from django.urls import path
from . import views

# HTPP Resquest <-> HTTP Response
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
