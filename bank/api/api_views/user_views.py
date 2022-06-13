from django.shortcuts import render

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import User
from ..serializers import UserSerializer


@api_view(['GET',])
def users(request):

    if request.method == 'GET':
        _users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response("Method not allowed", status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    _user = None
    try:
        _user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(_user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Method not allowed", status=status.HTTP_501_NOT_IMPLEMENTED)


class UserList(APIView):
    """
    List all bank users
    """
    def get(self, request, format=None):
        _users = User.objects.all()
        serializer = UserSerializer(_users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance.
    """
    model = User

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        _user = self.get_object(pk)
        serializer = UserSerializer(_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        _user = self.get_object(pk)
        _user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


