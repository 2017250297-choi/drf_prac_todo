from rest_framework import serializers
from todolists.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source="user_id")

    class Meta:
        model = TodoList
        exclude = ("user_id",)


class TodoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = [
            "title",
        ]
