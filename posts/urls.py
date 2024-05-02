from posts.apps import PostsConfig
from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

app_name = PostsConfig.name


urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='create_list_post'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_delete_post')
]
