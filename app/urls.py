from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='home'),
    path("update_task/<str:id>/",views.update,name='update_task'),
    path("delete_task/<str:id>/",views.delete,name='delete_task')
]
