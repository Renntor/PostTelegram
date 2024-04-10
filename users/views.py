from rest_framework import generics
from .models import User
from rest_framework.permissions import IsAdminUser
from .serializer import UserSerializers


class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializers


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializers
