from django.urls import path
from .views import TaskList
from . import views

urlpatterns = [
    path('',views.TaskList.as_view(),name='tasks'),
]