from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo
from .forms import TodoModelForm, DeleteConfirmForm


# Create your views here.
def index(request):
    # SELECT * FROM Todo
    todos = Todo.objects.all()

    return render(request, 'todos/index.html', {'todos': todos})


@login_required
def new(request):
    form = TodoModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # # save without write into database
        # todo = form.save(commit=False)
        # todo.creator = request.user
        # # save and write into database
        # todo.save()
        # form.save_m2m()
        todo = form.save(request.user)
        return redirect('todo:index')

    return render(request, 'todos/new.html', {'form': form})


def show(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/show.html', {'todo': todo})


@login_required
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoModelForm(request.POST or None, request.FILES or None, instance=todo)
    if form.is_valid():
        todo = form.save(request.user)
        return redirect('todo:show', pk)

    return render(request, 'todos/edit.html', {'form': form})


@login_required
def delete(request, pk):
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check'] == True:
        post = get_object_or_404(Todo, pk=pk)
        post.delete()
        return redirect('todo:index')

    return render(request, 'todos/delete.html', {'form': form})
