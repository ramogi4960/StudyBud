from django.forms import ModelForm
from .models import Topic, Room, Comment
from django.contrib.auth.models import User


class FormTopic(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class FormRoom(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["creator", "participants"]


class FormComment(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"


class FormUser(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
