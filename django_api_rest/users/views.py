from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
