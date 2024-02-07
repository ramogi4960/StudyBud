from django.shortcuts import render, redirect
from .forms import FormTopic, FormRoom, FormComment
from .models import Topic, Room, Comment
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
    context = {
        "form": UserCreationForm(),
    }
    return render(request, "user_registration.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "wrong password")

    return render(request, "user_login.html")


@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return redirect("user_login")


@login_required(login_url="user_login")
def homepage(request):
    q = request.GET.get("q") if request.GET.get("q") else ""

    context = {
        "rooms": Room.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(details__icontains=q) |
            Q(creator__username__icontains=q)
        ),
        "topics": Topic.objects.all(),
        "comments": Comment.objects.all(),
    }
    return render(request, "homepage.html", context)


@login_required(login_url="user_login")
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


@login_required(login_url="user_login")
def create_room(request):
    if request.method == "POST":
        form = FormRoom(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.creator = request.user
            room.save()
            return redirect("homepage")
    context = {
        "form": FormRoom(),
    }
    return render(request, "create_room.html", context)


@login_required(login_url="user_login")
def view_room(request, pk):
    if request.method == "POST":
        comment = Comment.objects.create(
            author=request.user,
            content=request.POST.get("comment"),
            room=Room.objects.get(id=pk),
        )
        comment.save()
        Room.objects.get(id=pk).participants.add(request.user)
        return redirect("view_room", pk=Room.objects.get(id=pk).id)
    context = {
        "room": Room.objects.get(id=pk),
        "comments": Room.objects.get(id=pk).comment_set.all().order_by("-updated"),
        "participants": Room.objects.get(id=pk).participants.all(),
    }
    return render(request, "view_room.html", context)


@login_required(login_url="user_login")
def edit_room(request, pk):
    if request.method == "POST":
        form = FormRoom(request.POST, instance=Room.objects.get(id=pk))
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        "form": FormRoom(instance=Room.objects.get(id=pk)),
    }
    return render(request, "edit_room.html", context)


@login_required(login_url="user_login")
def delete_room(request, pk):
    if request.method == "POST":
        Room.objects.get(id=pk).delete()
        return redirect("homepage")
    context = {
        "room": Room.objects.get(id=pk),
    }
    return render(request, "delete_room.html", context)


