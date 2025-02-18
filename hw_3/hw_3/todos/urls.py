from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]

