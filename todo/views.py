from django.shortcuts import get_object_or_404, render, redirect
from .forms import TodoForm
from django.http import HttpRequest
from django.contrib import messages
from .models import Todo


# Create your views here.
def get_all_todos(request: HttpRequest):
    todos = Todo.objects.all()
    return render(request, "todo/all_todos.html", {"todos": todos})


def get_todo(request: HttpRequest, pk: int):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "todo/todo.html", {"todo": todo})


def create_todo(request: HttpRequest):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo created successfully")
            return redirect("get_all_todos")  # adjust to your URL name
    else:
        form = TodoForm()
    return render(request, "todo/create_todo.html", {"form": form})


def update_todo(request: HttpRequest, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.info(request, "Todo updated successfully")
            return redirect("get_all_todos")  # change to your list page
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo/update_todo.html", {"form": form, "todo": todo})


def delete_todo(request: HttpRequest, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":  # user confirmed deletion
        todo.delete()
        messages.warning(request, "Todo deleted successfully")
        return redirect("get_all_todos")  # redirect to your list page
    # otherwise show confirmation page
    return render(request, "todo/confirm_delete.html", {"todo": todo})
