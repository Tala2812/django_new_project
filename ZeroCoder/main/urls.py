from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name='home'),  # Добавьте этот путь для корневого URL
    path('data', views.data, name='data'),
    path('test', views.test, name='test'),
]