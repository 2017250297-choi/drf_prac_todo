from rest_framework.views import APIView
from rest_framework import status, permissions
from users.permissions import IsOwnerOrReadOnly, IsExsistDeleteXorCreateOnly
from rest_framework.response import Response
from users.serializers import (
    UserSerializer,
    UserEditSerializer,
    CustomTokenObtainPairSerializer,
    UserAllInfoSerializer,
    UserLimitInfoSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from todolists.serializers import TodoListSerializer
from users.models import User
from rest_framework.generics import get_object_or_404


# Create your views here.
class UserView(APIView):
    permission_classes = (IsExsistDeleteXorCreateOnly,)

    def post(self, request):
        user_serialized = UserSerializer(data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            new_user = UserAllInfoSerializer(user_serialized.data)
            return Response(new_user.data, status=status.HTTP_201_CREATED)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user = User.objects.get(id=user.id)
        user.delete()
        return Response(
            {"message": "delete_success"}, status=status.HTTP_204_NO_CONTENT
        )


class UserInfoView(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        todo_serialized = TodoListSerializer(user.my_todolist, many=True)
        # check same person
        if user == request.user:
            user_serialized = UserAllInfoSerializer(user)
        else:
            user_serialized = UserLimitInfoSerializer(user)

        return Response(
            {"user": user_serialized.data, "users_todolist": todo_serialized.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(self.request, user)
        user_serialized = UserEditSerializer(user, data=request.data, partial=True)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtaionPairVeiw(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"success": "yes"}, status=status.HTTP_200_OK)
