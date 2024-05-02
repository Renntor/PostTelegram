from rest_framework import generics
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializer import PostSerializers
from .permission import IsUser


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsUser]
    serializer_class = PostSerializers
