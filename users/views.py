from rest_framework import viewsets, permissions

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
