from django.urls import path
from . import views

urlpatterns = [
    path("sql/", views.sql_learning),
]
