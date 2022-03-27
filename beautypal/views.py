from django.shortcuts import render
from .models import Room
from .forms import RoomForm


#rooms = [
 #   {'id': 1, 'name': 'Lets talk skincare!'},
  #  {'id': 2, 'name': 'Best haircare chat'},
   # {'id': 3, 'name': 'Makeup and color'},
#]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'beautypal/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'beautypal/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form': form}
    return render(request, 'beautypal/room_form.html', context)
    
    
def navbar(request):
    return render(request, 'navbar.html')
    
    # Create your views here.
