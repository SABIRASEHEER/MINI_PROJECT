from django.shortcuts import render
from django.http import HttpResponse
from bike.models import Bike
# Create your views here.
def post_bike(request):
    if request.method == "POST":
        obj=Bike()
        obj.name=request.POST.get('name')
        obj.model=request.POST.get('model')
        obj.price=request.POST.get('price')
        obj.conditions=request.POST.get('condition')
        obj.availability=request.POST.get('availability')
        obj.status='pending'
        obj.save()

    return render(request, 'bike/bike.html')

def view_bike(request):
    obj=Bike.objects.all()
    context={
        'x':obj
    }
    return render(request, 'bike/view.html', context)


def update(request,idd):
    obj=Bike.objects.get(b_id=idd)
    context={
        'x':obj
    }
    if request.method == "POST":
        obj=Bike.objects.get(b_id=idd)
        obj.name=request.POST.get('name')
        obj.model=request.POST.get('model')
        obj.price=request.POST.get('price')
        obj.conditions=request.POST.get('condition')
        obj.availability=request.POST.get('availability')
        obj.save()
        return view_bike(request)
    return render(request, 'bike/update.html',context)


def delete(request,idd):
    obj=Bike.objects.get(b_id=idd)
    obj.delete()
    return view_bike(request)

