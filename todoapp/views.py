from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone

from .models import ToDoItem


# Create your views here.

def todo_signup(request):
    messages = []
    context = {
        'messages': messages,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        password = request.POST.get('password')
        user = User.objects.create_user(username,
                                        email,
                                        password)
        print(user)
        if user is not None:
            messages.append(f'Hi {username}, Account Created, Please Login')
            return render(request, 'todoapp/login.html', context=context)
        else:
            messages.append(f'Hi {username}, Invalid data, Please Retry')
    return render(request, 'todoapp/signup.html', context=context)


def todo_login(request):
    messages = []
    context = {
        'messages': messages,
    }
    if request.user.is_authenticated:
        return redirect('todoapp:user_home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        context['username'] = username
        if user is not None:
            login(request, user)
            messages.append(f'Welcome {username}')
            return redirect('todoapp:user_home')
        else:
            messages.append('Invalid Credentials, Please Retry!')

    return render(request, 'todoapp/login.html', context)


def add_todo(request):
    context = {
        'messages': [],
    }
    if request.method == 'POST':
        todo_text = request.POST.get('todo_text')
        if len(todo_text) > 0:
            ToDoItem.objects.create(owner=request.user, todo_text=todo_text)
            context['messages'].append("Item added to TODO Successfully")
        else:
            context['messages'].append("ERROR adding item to TODO - Please Retry")
    return redirect('todoapp:user_home')


def home(request):
    if not request.user.is_authenticated:
        return redirect('todoapp:login')
    current_user = request.user
    incomplete_todos = current_user.todos.filter(completed=False).order_by('-created_date')
    complete_todos = current_user.todos.filter(completed=True).order_by('-completed_date')
    context = {
        'incomplete_todos': incomplete_todos,
        'complete_todos': complete_todos,
        'username': current_user.username,
    }
    return render(request, 'todoapp/home.html', context)


def todo_done(request, pk):
    task = request.user.todos.get(id=pk)
    task.completed = True
    task.completed_date = timezone.now()
    task.save()
    return redirect('todoapp:user_home')
