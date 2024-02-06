from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("create_topic", views.create_topic, name="create_topic"),
    path("create_room", views.create_room, name="create_room"),
]