from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from task5.models import Post
from task5.permissions import IsOwnerPermission
from task5.serializers import PostSerializers


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated,IsOwnerPermission]