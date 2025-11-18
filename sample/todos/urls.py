from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.create_todo, name='create_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('progress/<int:id>/', views.progress_todo, name='progress_todo'),
    path('complete/<int:id>/', views.complete_todo, name='complete_todo'),
]
