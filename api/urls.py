from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView, name="api-overview"),
    path('task-list/',views.taskList, name="task-list")
]