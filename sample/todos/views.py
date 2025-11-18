from django.shortcuts import render, get_object_or_404, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todos/todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})



def progress_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.status == 'pending':
        todo.status = 'in_progress'
    elif todo.status == 'in_progress':
        todo.status = 'completed'
    elif todo.status == 'completed':
        todo.status = 'pending'
    todo.save()
    return redirect('todo_list')

def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()  # As per user request, complete button deletes the task
    return redirect('todo_list')
