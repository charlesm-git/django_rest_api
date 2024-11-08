from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdminOrSelf


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminOrSelf]

    def perform_create(self, serializer):
        """Creates a User, hash its password and saves it"""
        user = serializer.save()
        password = serializer.validated_data.get("password")
        if password:
            user.set_password(password)
            user.save()
