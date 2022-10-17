from django.shortcuts import render

# Create your views here.
def post_login(request):
    return render(request,'login/login.html')