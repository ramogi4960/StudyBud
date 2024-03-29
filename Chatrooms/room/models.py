from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    details = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    participants = models.ManyToManyField(UserModel, related_name="participants", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.content[:50]
