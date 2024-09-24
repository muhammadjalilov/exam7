from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from task1.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Userni tekshiradi agar is deleted True bulsa token qaytarmaydi
    """
    @classmethod
    def get_token(cls, user):
        if user.is_deleted:
            raise ValidationError('No such user')
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id

        return token