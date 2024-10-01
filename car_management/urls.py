from django.urls import path
from . import views


urlpatterns = [
	path('cars/', views.car_list, name='car_list'),
	path('cars/register', views.register_car, name='register_car'),
]
