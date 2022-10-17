from django.shortcuts import render

# Create your views here.
def post_complaint(request):
    return render(request,'complaint/complaint.html')

def view_complaint(request):
    return render(request,'complaint/view.html')

def post_reply(request):
    return render(request,'complaint/reply.html')


def view_reply(request):
    return render(request,'complaint/view_reply.html')
