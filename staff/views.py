from django.shortcuts import render
from staff.models import Staff
# Create your views here.


# Create your views here.
def post_staff(request):
    if request.method == "POST":
        obj=Staff()
        obj.staffname=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.salary_day=request.POST.get('salary')
        obj.day_present=request.POST.get('day')
        obj.category=request.POST.get('category')
        obj.phone=request.POST.get('phn')

        obj.save()
    return render(request,'staff/staff.html')

def view_staff(request):
    obj=Staff.objects.all()
    context = {
        'x' : obj
    }
    return render(request, 'staff/view.html',context)

def update(request, idd):
    obj = Staff.objects.get(s_id=idd)
    context = {
        'x': obj
    }
    if request.method == "POST":
        obj=Staff.objects.get(s_id=idd)
        obj.staffname=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.salary_day=request.POST.get('salary')
        obj.day_present=request.POST.get('day')
        obj.category=request.POST.get('category')
        obj.phone=request.POST.get('phn')
        obj.save()
        return view_staff(request)

    return render(request,'staff/update.html',context)

def delete(request,idd):
    obj=Staff.objects.get(s_id=idd)
    obj.delete()
    return view_staff(request)

