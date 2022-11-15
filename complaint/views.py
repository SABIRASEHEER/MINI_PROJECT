from django.shortcuts import render
import datetime
# Create your views here.
from complaint.models import Complaint
from user.models import User

def post_complaint(request):
    ob=User.objects.all()
    context={
        'u':ob
    }
    if request.method== "POST":
        obj=Complaint()
        obj.complaint=request.POST.get('complaint')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.u_id=request.POST.get('ee')
        obj.replydate='1'
        obj.replytime='1'
        obj.save()
    return render(request,'complaint/complaint.html',context)

def view_complaint(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }

    return render(request,'complaint/view.html',context)


def post_reply(request,idd):
    if request.method == "POST":
        obj=Complaint.objects.get(c_id=idd)
        obj.response=request.POST.get('reply')
        obj.replytime=datetime.datetime.now()
        obj.replydate=datetime.datetime.today()
        obj.save()
    return render(request,'complaint/reply.html')


def view_reply(request):
    obj = Complaint.objects.all()
    context = {
        'y': obj
    }
    return render(request,'complaint/view_reply.html',context)
