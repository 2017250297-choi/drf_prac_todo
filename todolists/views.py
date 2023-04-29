from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions
from todolists.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from todolists.models import TodoList
from rest_framework.generics import get_object_or_404
from todolists.serializers import (
    TodoListSerializer,
    TodoListCreateSerializer,
)
from drf_yasg.utils import swagger_auto_schema


# from django.db.models.query_utils import Q
# Create your views here.
class TodoListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        todolist = TodoList.objects.all()
        serializer = TodoListSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TodoListCreateSerializer)
    def post(self, request):
        serializer = TodoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoSpecificView(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    @swagger_auto_schema(request_body=TodoListCreateSerializer)
    def put(self, request, todo_id):
        todo = get_object_or_404(TodoList, id=todo_id)
        self.check_object_permissions(self.request, todo)
        serializer = TodoListCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id):
        todo = get_object_or_404(TodoList, id=todo_id)
        self.check_object_permissions(self.request, todo)
        todo.delete()
        return Response("Account Deleted.", status=status.HTTP_200_OK)


class TodoCompleteView(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def put(self, request, todo_id):
        todo = get_object_or_404(TodoList, id=todo_id)
        self.check_object_permissions(self.request, todo)
        if todo.is_complete:
            todo.is_complete = False
        else:
            todo.is_complete = True
        todo.save()
        serializer = TodoListSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
