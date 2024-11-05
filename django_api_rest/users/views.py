from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdminOrSelf


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminOrSelf]
