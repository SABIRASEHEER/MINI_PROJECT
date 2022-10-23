from django.shortcuts import render
from login.models import Login
# Create your views here.
def post_login(request):
    obj=Login()
    obj.uname = request.POST.get('uname')
    obj.password = request.POST.get('psw')
    obj.type = request.POST.get('price')
    obj.status = ('condition')

    obj.save()
    return render(request,'login/login.html')