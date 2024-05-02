from django.urls import path
from users.apps import UsersConfig
from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    # user
    path('', UserListCreateAPIView.as_view(), name='create_list_user'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_destroy_user'),

    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
