from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<champion_name>/', views.detail, name='detail'),
]