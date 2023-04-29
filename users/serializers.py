from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        del validated_data["password2"]
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["name"] = user.name
        token["age"] = user.age
        token["gender"] = user.gender

        return token


class UserEditSerializer(UserSerializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        exclude = ("email",)

    def update(self, instance, validated_data):
        validated_data.pop("password2", None)
        validated_data.pop("current_password", None)
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])
            validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        return user

    def validate(self, attrs):
        if not self.instance.check_password(attrs.get("current_password")):
            raise serializers.ValidationError(
                {"current password": "current password wrong."}
            )
        return super().validate(attrs)


class UserAllInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "age",
            "gender",
            "introduction",
            "last_login",
        )


class UserLimitInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "introduction",
        )
