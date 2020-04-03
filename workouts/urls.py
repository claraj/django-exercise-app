from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_home, name='workout_home'),
    path('list', views.workout_list, name='workout_list'),
    path('details/<int:pk>', views.workout_detail, name='workout_detail'),
    path('delete/<int:pk>', views.workout_delete, name='workout_delete'),
    path('add', views.workout_add, name='workout_add')
]