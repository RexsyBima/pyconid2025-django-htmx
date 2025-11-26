from . import views
from django.urls import path, include

urlpatterns = [
    path("all/", views.get_all_todos, name=views.get_all_todos.__name__),
    path("get/<int:pk>", views.get_todo, name=views.get_todo.__name__),
    path("update/<int:pk>", views.update_todo, name=views.update_todo.__name__),
    path("create/", views.create_todo, name=views.create_todo.__name__),
    path("delete/<int:pk>", views.delete_todo, name=views.delete_todo.__name__),
]
