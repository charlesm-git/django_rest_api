from rest_framework.serializers import ModelSerializer, ValidationError

from datetime import date

from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "date_of_birth",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate_date_of_birth(self, value):
        """
        Validate that the user is older that 15 before creating the account
        """
        today = date.today()
        age = (today - value).days // 365
        if age < 15:
            raise ValidationError('User must be at least 15 years old')
        return value
