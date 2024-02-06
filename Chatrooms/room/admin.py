from django.contrib import admin
from .models import Topic, Room, Comment

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Comment)
