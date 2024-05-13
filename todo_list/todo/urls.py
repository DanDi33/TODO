from django.urls import path
from .views import home, TaskList

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskList.as_view(), name='tasks')
]