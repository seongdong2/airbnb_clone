from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

def room_detail(request, pk):
    room = models.Room.objects.get(pk=pk)
    return render(request, "rooms/detail.html", {"room": room})