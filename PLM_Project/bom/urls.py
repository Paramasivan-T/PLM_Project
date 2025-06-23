from django.urls import path
from . import views

urlpatterns = [
    path('', views.bom_home, name='bom_home'),
    path('<int:part_id>/', views.bom_detail, name='bom_detail'),
]
