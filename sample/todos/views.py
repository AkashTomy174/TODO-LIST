from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TodoForm
from .models import Todo

# Create your views here.
@login_required
def todo_list(request):
    # Show only todos belonging to the logged-in user
    todos = Todo.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})



@login_required
def progress_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.owner != request.user:
        return HttpResponseForbidden()
    if todo.status == 'pending':
        todo.status = 'in_progress'
    elif todo.status == 'in_progress':
        todo.status = 'completed'
    elif todo.status == 'completed':
        todo.status = 'pending'
    todo.save()
    return redirect('todo_list')

@login_required
def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.owner != request.user:
        return HttpResponseForbidden()
    todo.delete()  # As per user request, complete button deletes the task
    return redirect('todo_list')
