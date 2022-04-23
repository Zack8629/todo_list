from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from tasks.views import TasksListView, TaskCreateView, TaskUpdateView

app_name = 'tasks'

urlpatterns = [
    path('', TasksListView.as_view(), name='index'),
    path('create_task/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('login/', LoginView.as_view(next_page='/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
