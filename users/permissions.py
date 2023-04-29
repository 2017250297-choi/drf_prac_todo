from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 user와 동일한지 확인
        return obj == request.user


class IsExsistDeleteXorCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(bool(request.user and request.user.is_authenticated))
        if request.method == "POST":
            print()
            return not bool(request.user and request.user.is_authenticated)
        elif request.method == "DELETE":
            return bool(request.user and request.user.is_authenticated)
