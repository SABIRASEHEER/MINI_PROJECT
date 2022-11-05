from django.shortcuts import render
from notification.models import Notification
# Create your views here.
from notification.models import Notification
import datetime
def post_notification(request):
    if request.method == "POST":
        obj=Notification()
        obj.notification=request.POST.get('notification')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')

def view_notification(request):
    obj=Notification.objects.all()
    context={
        'x': obj
    }
    return render(request, 'notification/view.html',context)
def delete(request, idd):
    obj = Notification.objects.get(n_id=idd)
    obj.delete()
    return view_notification(request)
