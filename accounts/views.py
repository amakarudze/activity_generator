from rest_framework import generics
from rest_framework.settings import api_settings

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
