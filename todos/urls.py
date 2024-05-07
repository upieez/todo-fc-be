from django.urls import path

from . import views

urlpatterns = [
    # Get, Post and Filter Todos
    path("", views.index, name="index"),
    # Mark / Unmark / Del Todo
    path("<int:id>/", views.update, name="update"),
    # Reorder Todos
    path("<int:id>/reorder", views.reorder, name="reorder"),
    # Delete All Completed Todos
    path("completed/", views.del_completed, name="del_completed"),
]