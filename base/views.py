from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Liverpool discussion.'},
#     {'id':2, 'name': 'Man City discussion.'},
#     {'id':3, 'name': 'Arsenal discussion.'}
# ]



def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context =  {'room':room}        

    return render(request,'base/room.html',context)
