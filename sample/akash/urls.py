
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name='index'),
   path('home/',views.home, name='home'),
   path('form/', views.form_view, name='form'),
   path('messages/', views.messages_view, name='messages'),
   path('edit/<int:id>/', views.edit_message, name='edit_message'),
   path('delete/<int:id>/', views.delete_message, name='delete_message'),
]
