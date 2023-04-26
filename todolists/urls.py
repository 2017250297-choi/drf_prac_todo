from django.urls import path
from todolists import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todolist"),
    path("<int:todo_id>/", views.TodoSpecificView.as_view(), name="todospecific"),
    path(
        "complete/<int:todo_id>/",
        views.TodoCompleteView.as_view(),
        name="todo_complete",
    ),
]
