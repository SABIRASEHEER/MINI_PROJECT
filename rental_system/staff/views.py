from django.shortcuts import render

# Create your views here.


# Create your views here.
def post_staff(request):
    return render(request,'staff/staff.html')

def view_staff(request):
        return render(request, 'staff/view.html')
