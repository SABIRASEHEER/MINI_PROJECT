from django.shortcuts import render
from request.models import Request
from django.core.files.storage import FileSystemStorage
from user.models import User
from bike.models import Bike
# Create your views here.

def post_request(request):
    ob1 = User.objects.all()
    ob2 = Bike.objects.all()
    context = {
        'u': ob1,
        'v': ob2
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
        obj.status='pendind'
        obj.u_id=request.POST.get('ee')
        obj.b_id=request.POST.get('ef')
        obj.save()
    return render(request,'request/request.html',context)

def view_request(request):
    obj=Request.objects.all()
    context={
        'x':obj
    }
    return render(request,'request/view.html',context)

def viewstatus(request):
    obj = Request.objects.all()
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