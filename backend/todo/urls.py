from django.urls import path
from .views import todo_patch,todo_api,new_todo

urlpatterns = [
    path("todo_list/", todo_api, name="todo-list"),
    path("<int:pk>/", todo_patch, name="todo-detail"),  
    path("new/",new_todo,name='new-todo')
]