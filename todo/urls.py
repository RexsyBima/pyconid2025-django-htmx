from . import views
from django.urls import path, include

urlpatterns = [
    path("all/", views.get_all_todos, name=views.get_all_todos.__name__),
    path("all_htmx/", views.get_all_todos_htmx, name=views.get_all_todos_htmx.__name__),
    path("get/<int:pk>", views.get_todo, name=views.get_todo.__name__),
    path("get_htmx/<int:pk>", views.get_todo_htmx, name=views.get_todo_htmx.__name__),
    path("update/<int:pk>", views.update_todo, name=views.update_todo.__name__),
    path(
        "update_htmx/<int:pk>",
        views.update_todo_htmx,
        name=views.update_todo_htmx.__name__,
    ),
    path("create/", views.create_todo, name=views.create_todo.__name__),
    path("create_htmx/", views.create_todo_htmx, name=views.create_todo_htmx.__name__),
    path(
        "create_htmx_v2/",
        views.create_todo_htmx_v2,
        name=views.create_todo_htmx_v2.__name__,
    ),
    path("delete/", views.delete_element, name=views.delete_element.__name__),
    path("delete/<int:pk>", views.delete_todo, name=views.delete_todo.__name__),
    path(
        "delete_todo_htmx/<int:pk>",
        views.delete_todo_htmx,
        name=views.delete_todo_htmx.__name__,
    ),
]
