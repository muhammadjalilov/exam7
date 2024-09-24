from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from task1.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise ValidationError('Passwords must be match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        users = User.objects.all()
        for user in users:
            if validated_data.get('username') == user.username and not user.is_deleted:
                user.is_deleted = True
                user.save()
                return user
        user: User = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
