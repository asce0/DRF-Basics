from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post


class test(APIView):

    # Authentication Permissions
    permission_classes = (IsAuthenticated,)

    # The Get Method Using API (Django Rest FrameWork)
    def get(self, request,*args, **kwargs ):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # The Post Method Using API (Django Rest FrameWork)
    def post(self, request,*args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
