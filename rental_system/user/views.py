from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def post_user(request):
    return render(request,'user/user.html')

def view_user(request):
    # return HttpResponse('dddd')
    return render(request, 'user/view.html')

