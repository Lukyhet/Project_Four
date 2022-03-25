from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': 'Lets talk skincare!'},
    {'id': 2, 'name': 'Best haircare chat'},
    {'id': 3, 'name': 'Makeup and color'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'beautypal/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'beautypal/room.html', context)
    
    
def navbar(request):
    return render(request, 'navbar.html')# Create your views here.
