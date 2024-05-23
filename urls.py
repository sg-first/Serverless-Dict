from django.urls import path

from . import views

urlpatterns = [
    path("manage/", views.manage, name="manage"),
    path("insert/", views.insert, name="insert")
]