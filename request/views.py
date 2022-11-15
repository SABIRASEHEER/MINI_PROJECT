from django.shortcuts import render
from pip._vendor.six import u

from request.models import Request
from django.core.files.storage import FileSystemStorage
from user.models import User
from bike.models import Bike
from payment.models import Payment
import datetime
# Create your views here.

def post_request(request,idd):
    ss=request.session["uid"]
    ob1 = User.objects.get(u_id=ss)
    ob2 = Bike.objects.get(b_id=idd)
    context = {
        'u': ob1,
        'p': ob2
    }
    if request.method == "POST":
        obj=Request()
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        # obj.document='1'
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.document=myfile.name
        obj.status='pending'
        obj.u_id=ss
        # obj.bikename=request.POST.get('bike')
        obj.b_id=idd
        obj.save()
    return render(request,'request/request.html',context)

def view_request(request):
    obj=Request.objects.all()
    context={
        'x':obj
    }
    return render(request,'request/view.html',context)

def viewstatus(request):
    ss = request.session["uid"]
    obj = Request.objects.filter(u_id=ss)
    context = {
        'x': obj
    }
    return render(request,'request/viewstatus.html',context)

def approve(request,idd):
    obj=Request.objects.get(r_id=idd)
    obj.status='approved'
    obj.save()
    return view_request(request)


def reject(request,idd):
    obj=Request.objects.get(r_id=idd)
    obj.status='rejected'
    obj.save()
    return view_request(request)


























def payment(request,idd):
    ob1 = User.objects.all()
    ob2 = Bike.objects.all()
    obj=Request.objects.get(r_id=idd)
    context={
        'u': ob1,
        'v': ob2,
        'x':obj
    }
    if request.method == 'POST':
        obj=Payment()
        obj.amount=request.POST.get('amount')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.u_id=request.POST.get('ee')
        obj.b_id=request.POST.get('ef')
        obj.save()
        return view_request(request)
    return render(request, 'payment/payment.html',context)
