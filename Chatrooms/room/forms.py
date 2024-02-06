from django.forms import ModelForm
from .models import Topic, Room, Comment


class FormTopic(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class FormRoom(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        # exclude = ["creator", "participants"]


class FormComment(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
