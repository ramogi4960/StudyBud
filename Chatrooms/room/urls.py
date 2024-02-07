from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("user_registration", views.user_registration, name="user_registration"),
    path("user_login", views.user_login, name="user_login"),
    path("user_logout", views.user_logout, name="user_logout"),
    path("user_profile/<int:pk>", views.user_profile, name="user_profile"),
    path("create_topic", views.create_topic, name="create_topic"),
    path("create_room", views.create_room, name="create_room"),
    path("view_room/<int:pk>", views.view_room, name="view_room"),
    path("edit_room/<int:pk>", views.edit_room, name="edit_room"),
    path("delete_room/<int:pk>", views.delete_room, name="delete_room"),
]