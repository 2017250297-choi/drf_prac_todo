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

    def validate(self, attrs):
        if len(attrs.get("title").strip()) < 3:
            raise serializers.ValidationError(
                {"title": "title needs to longer than 2 letters."}
            )
        return super().validate(attrs)
