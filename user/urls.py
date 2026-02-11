from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/favourite/', views.Ufavouriteapiview.as_view()),
    path('user/cart/', views.Ucartapiview.as_view()),
    path('post/', views.PostListCreateAPIView.as_view()),
    path('postd/', views.PostDetailAPIView.as_view()),
    
]
