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
            raise ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        existing_user = User.objects.filter(username=validated_data.get('username'), is_deleted=False).first()

        if existing_user:
            raise ValidationError({"username": "Username already exists"})

        deleted_user = User.objects.filter(username=validated_data.get('username'), is_deleted=True).first()

        if deleted_user:
            deleted_user.is_deleted = False
            deleted_user.set_password(validated_data.get('password'))
            deleted_user.email = validated_data.get('email')
            deleted_user.save()
            return deleted_user

        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
