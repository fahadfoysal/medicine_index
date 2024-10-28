from django.urls import path
from .views import (
    medicine_list,
    medicine_create,
    medicine_update,
    medicine_delete,
    user_login,
    user_logout,
    register,
)

urlpatterns = [
    path('', medicine_list, name='medicine_list'),
    path('create/', medicine_create, name='medicine_create'),
    path('update/<int:pk>/', medicine_update, name='medicine_update'),
    path('delete/<int:pk>/', medicine_delete, name='medicine_delete'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
]
