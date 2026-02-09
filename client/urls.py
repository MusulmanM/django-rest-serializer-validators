from django.urls import path
from .views import Mijozapiview




urlpatterns = [
    path('client/', Mijozapiview.as_view(), name='client'),
]