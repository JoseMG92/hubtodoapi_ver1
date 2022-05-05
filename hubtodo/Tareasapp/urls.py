from django.urls import re_path
from Tareasapp import views

urlpatterns = [
    re_path(r'^tarea$', views.tareas_api)
]