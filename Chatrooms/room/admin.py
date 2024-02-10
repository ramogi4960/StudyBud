from django.contrib import admin
from .models import Topic, Room, Comment, UserModel

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(UserModel)
