from django.urls import path
from .views import todo_signup, todo_login, add_todo, home, todo_done
from django.contrib.auth.views import LogoutView
from django.conf import settings


app_name = 'todoapp'
urlpatterns = [
    path('', todo_login, name='home'),
    path('signup/', todo_signup, name='signup'),
    path('login/', todo_login, name='login'),
    path('add_todo/', add_todo, name='add_todo'),
    path('home/', home, name='user_home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todo_done/<int:pk>/', todo_done, name='todo_done'),
]
