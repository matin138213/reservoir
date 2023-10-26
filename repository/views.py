from rest_framework.viewsets import ModelViewSet

from .models import User, Password
from .serializers import PasswordSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PasswordViewSet(ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
