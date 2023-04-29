from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 todolist user_id와 동일한지 확인
        print(obj.user_id == request.user)
        return obj.user_id == request.user
