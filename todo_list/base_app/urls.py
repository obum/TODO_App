from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', view=CustomLoginView.as_view() , name='login'),
    path('logout/', view=LogoutView.as_view(next_page='login') , name='logout'),
    path('register/', view=RegisterPage.as_view() , name='register'),
    path('', view=TaskList.as_view() , name='tasks'),
    path('task/<int:pk>/', view=TaskDetail.as_view() , name='task'),
    path('task-create/', view=TaskCreate.as_view() , name='task-create'),
    path('task-update/<int:pk>', view=TaskUpdate.as_view() , name='task-update'),
    path('task-delete/<int:pk>', view=TaskDelete.as_view() , name='task-delete'),
    ]