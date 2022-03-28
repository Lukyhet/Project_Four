from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm


#rooms = [
 #   {'id': 1, 'name': 'Lets talk skincare!'},
  #  {'id': 2, 'name': 'Best haircare chat'},
   # {'id': 3, 'name': 'Makeup and color'},
#]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''

    rooms = Room.objects.filter(
       Q(topic__name__icontains=q) |
       Q(name__icontains=q) |
       Q(description__icontains=q)

    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'beautypal/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'beautypal/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'beautypal/room_form.html', context)
    
    
def navbar(request):
    return render(request, 'navbar.html')
    

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'beautypal/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'beautypal/delete.html', {'obj': room})
    

    

    
    # Create your views here.
