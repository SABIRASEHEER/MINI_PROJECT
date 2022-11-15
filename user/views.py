from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def post_user(request):
    if request.method == "POST":
        obj=User()
        obj.username = request.POST.get('un')
        obj.uaddress = request.POST.get('address')
        obj.aadharnum = request.POST.get('adhar')
        obj.licensenum = request.POST.get('license')
        obj.pancardno = request.POST.get('pancard')
        obj.gender = request.POST.get('gender')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.password=request.POST.get('p')
        obj.status='pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type='user'
        ob.status='pending'
        ob.u_id=obj.u_id
        ob.save()




        obj.save()
    return render(request,'user/user.html')

def view_user(request):
    # return HttpResponse('dddd')
    obj=User.objects.all()
    context={
        'x':obj
    }
    return render(request, 'user/view.html',context)

def approve(request,idd):
    obk=User.objects.get(u_id=idd)
    obk.status='approved'
    obk.save()
    ob=Login.objects.get(u_id=idd)
    ob.status="approved"
    ob.save()
    return view_user(request)






