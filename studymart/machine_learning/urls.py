from django.urls import path
from . import views

urlpatterns = [
    path("ml/", views.machine_learning),
]
