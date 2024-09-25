from django.urls import path
from .import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('createtask/', views.createTask, name='createtask'),
    path('updatetask/<int:task_id>', views.updateTask, name='updatetask'),
    path('deletetask/<int:task_id>', views.deleteTask , name='deletetask'),
    path('tasklist/', views.taskList, name='tasklist'),
    path('taskfilter/', views.TaskListView.as_view(), name='taskfilter'),
]
