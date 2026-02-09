from django.urls import path
from .views import Catapiview, Proapiview



urlpatterns = [
    path("category/", view=Catapiview.as_view()),
    path("product/", view=Proapiview.as_view()),
]