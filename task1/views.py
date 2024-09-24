from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from task1.models import User
from task1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    is_deletedni tekshirish uchun methodlarni overrride qildim
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        instance: User = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return Response({'message': 'No such user'})
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return Response({'message': 'No such user'})
        return super().partial_update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = User.objects.filter(is_deleted=False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return Response({'message': 'No such user'})
        return super().retrieve(request, *args, **kwargs)
