from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoForm

def home_page(request):
    return render(request, "templates/todo/home_page.html")

def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to the home page
    else:
        form = ToDoForm()
    return render(request, 'todo/add_todo.html', {'form': form})