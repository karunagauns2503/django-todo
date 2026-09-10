from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()

        if title:
            Todo.objects.create(title=title)

        return redirect("todo_list")

    todos = Todo.objects.all().order_by("-id")

    return render(
        request,
        "todos/todo_list.html",
        {"todos": todos},
    )


def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    todo.completed = not todo.completed
    todo.save()

    return redirect("todo_list")


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    todo.delete()

    return redirect("todo_list")
