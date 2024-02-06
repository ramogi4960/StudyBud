from django.shortcuts import render, redirect
from .forms import FormTopic, FormRoom, FormComment
from .models import Topic, Room, Comment


def homepage(request):
    context = {
        "rooms": Room.objects.all(),
    }
    return render(request, "homepage.html", context)


def create_topic(request):
    if request.method == "POST":
        form = FormTopic(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        "form": FormTopic(),
    }
    return render(request, "create_topic.html", context)


def create_room(request):
    if request.method == "POST":
        form = FormRoom(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            # form.creator = request.user
            form.save()
            return redirect("homepage")
    context = {
        "form": FormRoom(),
    }
    return render(request, "create_room.html", context)


