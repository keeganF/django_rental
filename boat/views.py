from django.shortcuts import render, redirect
from  .models import Boat

# Create your views here.
def index(request):
    boats = Boat.objects.all()
    return render(request, 'boat/index.html', {
        'items': boats
    })

def home(request):
    return render(request, 'boat/home.html')

def rent(request, item_id):
    item = Boat.objects.get(pk=item_id)
    item.quantity -= 1
    item.save()
    return redirect('index')

def return_item(request, item_id):
    item = Boat.objects.get(pk=item_id)
    item.quantity += 1
    item.save()
    return redirect('index')