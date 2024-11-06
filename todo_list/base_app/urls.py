from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', view=TaskList.as_view() , name='tasks'),
    path('task/<int:pk>/', view=TaskDetail.as_view() , name='task'),
    path('task-create/', view=TaskCreate.as_view() , name='task-create'),
    path('task-update/<int:pk>', view=TaskUpdate.as_view() , name='task-update'),
     path('task-delete/<int:pk>', view=TaskDelete.as_view() , name='task-delete'),
]