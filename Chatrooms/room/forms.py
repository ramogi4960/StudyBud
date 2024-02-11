from django.forms import ModelForm
from .models import Topic, Room, Comment, UserModel
from django.contrib.auth.forms import UserCreationForm


class FormUserRegistration(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["name", "username", "email", "password1", "password2"]


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


class FormUserModel(ModelForm):
    class Meta:
        model = UserModel
        fields = ["name", "username", "email", "avatar", "bio"]
