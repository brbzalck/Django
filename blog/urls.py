from django.urls import path
from . import views

# HTPP Resquest <-> HTTP Response
app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
