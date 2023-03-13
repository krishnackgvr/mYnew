from django.shortcuts import render
from django.shortcuts import render
from . models import Place,Item
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    item=Item.objects.all()
    return render(request,"index.html",{'result':obj,'item':item})


