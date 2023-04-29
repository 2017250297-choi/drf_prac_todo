from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.urls import path
from users import views

urlpatterns = [
    path("", views.UserView.as_view(), name="user_view"),
    path("<int:user_id>/", views.UserInfoView.as_view(), name="user_info_view"),
    path(
        "token/",
        views.CustomTokenObtaionPairVeiw.as_view(),
        name="token_obtain_view",
    ),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
]
