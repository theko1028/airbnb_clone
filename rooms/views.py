from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 5, orphans=2)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"rooms": rooms})
    except EmptyPage:
        return redirect("/")
