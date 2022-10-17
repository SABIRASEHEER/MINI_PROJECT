from django.shortcuts import render

# Create your views here.
def post_notification(request):
    return render(request,'notification/notification.html')

def view_notification(request):
        return render(request, 'notification/view.html')
