from django.shortcuts import render
from request.models import Request
from django.core.files.storage import FileSystemStorage
# Create your views here.

def post_request(request):
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
        obj.u_id='1'
        obj.b_id='1'
        obj.save()
    return render(request,'request/request.html')

def view_request(request):
    return render(request,'request/view.html')

def viewstatus(request):
    return render(request,'request/request.html')